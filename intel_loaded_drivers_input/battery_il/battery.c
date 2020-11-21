/**
*** INTEL CONFIDENTIAL
***
*** Copyright (March 2011) (March 2011) Intel Corporation All Rights Reserved.
*** The source code contained or described herein and all documents related to the
*** source code ("Material") are owned by Intel Corporation or its suppliers or
*** licensors. Title to the Material remains with Intel Corporation or its
*** suppliers and licensors. The Material contains trade secrets and proprietary
*** and confidential information of Intel or its suppliers and licensors.
*** The Material is protected by worldwide copyright and trade secret laws
*** and treaty provisions. No part of the Material may be used, copied,
*** reproduced, modified, published, uploaded, posted, transmitted, distributed,
*** or disclosed in any way without Intel's prior express written permission.
***
*** No license under any patent, copyright, trade secret or other intellectual
*** property right is granted to or conferred upon you by disclosure or delivery
*** of the Materials, either expressly, by implication, inducement, estoppel or
*** otherwise. Any license under such intellectual property rights must be
*** express and approved by Intel in writing.
**/
//-----------------------------------------------------------------------------
// Headers inclusions.
//-----------------------------------------------------------------------------
#include <assert.h>
#include "battery.h"
#include <windows.h>

//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
// Global counter.
//-----------------------------------------------------------------------------
BOOL status;
// initialize the numbers of status
SYSTEM_POWER_STATUS statusList = { 1, 255, 255, 0, -1, 1 };

/*-----------------------------------------------------------------------------
Function: modeler_init_inputs
Purpose : return the inputs count.
*/

ESRV_API ESRV_STATUS modeler_init_inputs(
	unsigned int *p,
	int *pfd,
	int *pfe,
	char *po,
	size_t so
) {
	SET_INPUTS_COUNT(INPUT_COUNT);
	return(ESRV_SUCCESS);
}

/*-----------------------------------------------------------------------------
Function: modeler_open_inputs
Purpose : open inputs.
In : pointer to PINTEL_MODELER_INPUT_TABLE data structure.
Out : modified PINTEL_MODELER_INPUT_TABLE data structure.
Return : status.
-----------------------------------------------------------------------------*/
ESRV_API ESRV_STATUS modeler_open_inputs(PINTEL_MODELER_INPUT_TABLE p) {

	//-------------------------------------------------------------------------
	// Input descriptions.
	//-------------------------------------------------------------------------

	static char *descriptions[INPUT_COUNT] = {
		INPUT_DESCRIPTION_STRINGS
	};

	static INTEL_MODELER_INPUT_TYPES input_types[INPUT_COUNT] = {
		INPUT_TYPES
	};
	// Exception handling section begin.
	//-------------------------------------------------------------------------
	INPUT_BEGIN_EXCEPTIONS_HANDLING
		assert(p != NULL);

	//-------------------------------------------------------------------------
	// Set input information.
	//-------------------------------------------------------------------------
	unsigned int i = 0;
	SET_INPUTS_NAME(INPUT_NAME_STRING);

	for (i = 0; i < INPUT_COUNT; i++) {

		//---------------------------------------------------------------------
		// BUILD_NORMAL_DESCRIPTION(b, z, s, c, x, m, u, y)
		// Arguments:
		//    + b: buffer to receive name.
		//    + z: buffer size in bytes.
		//    + s: string containing the input's system level category.
		//    + c: string containing the input's component name.
		//    + x: string containing the input's sub-component name.
		//    + m: string containing the input's metric name.
		//    + u: string containing the input's unit.
		//    + y: string containing the input's optional id.
		//---------------------------------------------------------------------

		SET_INPUT_DESCRIPTION(
			i,
			descriptions[i]
		);
		SET_INPUT_TYPE(
			i,
			input_types[i]
		);

	};
	return(ESRV_SUCCESS);
	//-------------------------------------------------------------------------
// Exception handling section end.
//-------------------------------------------------------------------------
	INPUT_END_EXCEPTIONS_HANDLING(p)

};

/*-----------------------------------------------------------------------------
Function: modeler_close_inputs
Purpose : close inputs.
In : pointer to PINTEL_MODELER_INPUT_TABLE data structure.
Out : modified PINTEL_MODELER_INPUT_TABLE data structure.
XLSDK
54 Intel Confidential
Return : status.
-----------------------------------------------------------------------------*/

ESRV_API ESRV_STATUS modeler_close_inputs(PINTEL_MODELER_INPUT_TABLE p) {
	assert(p != NULL);
	return(ESRV_SUCCESS);
}

/*-----------------------------------------------------------------------------
Function: modeler_read_inputs
Purpose : collect all inputs.
In : pointer to PINTEL_MODELER_INPUT_TABLE data structure.
Out : modified PINTEL_MODELER_INPUT_TABLE data structure.
Return : status.
-----------------------------------------------------------------------------*/
extern ESRV_STATUS modeler_read_inputs(PINTEL_MODELER_INPUT_TABLE p) {
	assert(p != NULL);
	//-------------------------------------------------------------------------
	// Generate incrementing input.
	//-------------------------------------------------------------------------
	status = GetSystemPowerStatus(&statusList);
	//-------------------------------------------------------------------------
	// Set input values.
	//-------------------------------------------------------------------------
	SET_INPUT_ULL_VALUE(
		INPUT_INDEX_AC,
		statusList.ACLineStatus
	);
	SET_INPUT_ULL_VALUE(
		INPUT_INDEX_LIFE,
		statusList.BatteryLifePercent
	);
	SET_INPUT_ULL_VALUE(
		INPUT_INDEX_SAVER,
		statusList.SystemStatusFlag
	);
	SET_INPUT_ULL_VALUE(
		INPUT_INDEX_TIME,
		statusList.BatteryLifeTime
	);
	return(ESRV_SUCCESS);
}
/*-----------------------------------------------------------------------------
Function: modeler_listen_inputs
Purpose : listen for all inputs.
In : pointer to PINTEL_MODELER_INPUT_TABLE data structure.
Out : modified PINTEL_MODELER_INPUT_TABLE data structure.
Return : status.
-----------------------------------------------------------------------------*/
extern ESRV_STATUS modeler_listen_inputs(PINTEL_MODELER_INPUT_TABLE p) {
	assert(p != NULL);
	return(ESRV_SUCCESS);
}

/*-----------------------------------------------------------------------------
Function: modeler_process_dctl
Purpose : process DCTL commands on DCTL interrupt notification.
In : pointer to PINTEL_MODELER_INPUT_TABLE data structure.
Out : modified PINTEL_MODELER_INPUT_TABLE data structure.
Return : status.
-----------------------------------------------------------------------------*/
ESRV_STATUS modeler_process_dctl(PINTEL_MODELER_INPUT_TABLE p) {
	assert(p != NULL);
	return(ESRV_SUCCESS);
}

/*-----------------------------------------------------------------------------
Function: modeler_process_lctl
Purpose : process LCTL commands on LCTL interrupt notification.
In : pointer to PINTEL_MODELER_INPUT_TABLE data structure.
Out : modified PINTEL_MODELER_INPUT_TABLE data structure.
Return : status.
-----------------------------------------------------------------------------*/
ESRV_STATUS modeler_process_lctl(PINTEL_MODELER_INPUT_TABLE p) {
	assert(p != NULL);
	return(ESRV_SUCCESS);
}







