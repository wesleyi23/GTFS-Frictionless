|  Field Name | Type | Required | Description |
|  ------ | ------ | ------ | ------ |
|  `fare_id` | ID | **Required** | Identifies a fare class. |
|  `price` | Non-negative float | **Required** | Fare price, in the unit specified by `currency_type`. |
|  `currency_type` | Currency code | **Required** | Currency used to pay the fare. |
|  `payment_method` | Enum | **Required** | Indicates when the fare must be paid. Valid options are:<br><br>`0` - Fare is paid on board.<br>`1` - Fare must be paid before boarding. |
|  `transfers` | Enum | **Required** | Indicates the number of transfers permitted on this fare. The fact that this field can be left empty is an exception to the requirement that a Required field must not be empty. Valid options are:<br><br>`0` - No transfers permitted on this fare.<br>`1` - Riders may transfer once.<br>`2` - Riders may transfer twice.<br>empty - Unlimited transfers are permitted. |
|  `agency_id` | ID referencing `agency.agency_id` | **Conditionally Required** | Identifies the relevant agency for a fare. This field is required for datasets with multiple agencies defined in [agency.txt](#agencytxt), otherwise it is optional. |
|  `transfer_duration` | Non-negative integer | Optional | Length of time in seconds before a transfer expires. When `transfers`=`0` this field can be used to indicate how long a ticket is valid for or it can be left empty. |