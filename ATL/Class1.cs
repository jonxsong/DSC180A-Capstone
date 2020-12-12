using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AnalyzerTask;
using Intel.DCA.Common;
using System.IO;
using System.Data;
using ATLHelper;


namespace BatteryAnalyzerTask
{
    public class Class1 : DBAnalyzerTaskBase
    {
        public const string ID = "BatteryAnalyzerTask";
        public Class1(List<string> dependencies, string paramString = null)
            : base(ID, dependencies, paramString)
        {
        }
        public override void Execute(AnalyzerTaskExecutionOptions options)
        {
            DBQueryEngine new_db_engine = null;

            try
            {
                ///  READING from merged file and inserting data into new DB file ..
                ///  Run queries from that DB file so as not to block other ATLs

                new_db_engine = new DBQueryEngine();

                String new_db_file = Path.Combine(options.CollectorDataLocation, "battery.atldb");

                new_db_engine.InitDBConnection(new_db_file, options.Logger);
                String attach_query = "ATTACH '" + options.IdcDatabaseFilename + "' AS IDC_DATABASE";

                new_db_engine.RunQuery(attach_query);

                String get_stats = @"select 'MIN', min(VALUE)
                                        from COUNTERS_ULL_TIME_DATA 
                                        WHERE ID_INPUT=1
                                        union
                                        select 'MAX', max(VALUE)
                                        from COUNTERS_ULL_TIME_DATA 
                                        WHERE ID_INPUT=1
                                        union
                                        select 'AVG', avg(VALUE)
                                        from COUNTERS_ULL_TIME_DATA WHERE ID_INPUT=1";

                //Runs the query string and stores the output in a DataTable

                DataTable table = new_db_engine.RetrieveTableData(get_stats);

                LogQueryResultsConfig battery_config = new LogQueryResultsConfig();
                battery_config.Prefix = options.SystemGuid; // system GUID
                battery_config.DirectoryPath = options.CollectorDataLocation;
                battery_config.FilenamePrefix = "BatteryAnalyzerTask";
                new_db_engine.logDataTableResults(battery_config, table);
            }
            catch (Exception e)
            {
                //options.Logger.Log(SvcLogger.LogLevel.ERROR, "Exception while running Battery analyzer task: " + e.ToString());
                this.LogAtlMessage(SvcLogger.LogLevel.ERROR, SvcLogger.AtlErrorCodes.ERROR_IN_PROCESSING, "Exception while running processAnalyzer analyzer task: " + e.ToString());
            }
            finally
            {
                if (new_db_engine != null)
                {
                    String dettach_query = "DETACH '" + options.IdcDatabaseFilename + "'";

                    //new_db_engine.RunQuery(dettach_query);
                    new_db_engine.CloseDBConnection();
                }
            }
        }
    }
}
