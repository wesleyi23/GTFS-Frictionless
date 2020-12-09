Dataset file,Field Name,Type,Required,Description
agency.txt,agency_id,ID,Conditionally Required,"Identifies a transit brand which is often synonymous with a transit agency. Note that in some cases, such as when a single agency operates multiple separate services, agencies and brands are distinct. This document uses the term ""agency"" in place of ""brand"". A dataset may contain data from multiple agencies. This field is required when the dataset contains data for multiple transit agencies, otherwise it is optional."
agency.txt,agency_name,Text,Required,Full name of the transit agency.
agency.txt,agency_url,URL,Required,URL of the transit agency.
agency.txt,agency_timezone,Timezone,Required,"Timezone where the transit agency is located. If multiple agencies are specified in the dataset, each must have the same agency_timezone."
agency.txt,agency_lang,Language code,Optional,Primary language used by this transit agency. This field helps GTFS consumers choose capitalization rules and other language-specific settings for the dataset.
agency.txt,agency_phone,Phone number,Optional,"A voice telephone number for the specified agency. This field is a string value that presents the telephone number as typical for the agency's service area. It can and should contain punctuation marks to group the digits of the number. Dialable text (for example, TriMet's ""503-238-RIDE"") is permitted, but the field must not contain any other descriptive text."
agency.txt,agency_fare_url,URL,Optional,URL of a web page that allows a rider to purchase tickets or other fare instruments for that agency online.
agency.txt,agency_email,Email,Optional,Email address actively monitored by the agency’s customer service department. This email address should be a direct contact point where transit riders can reach a customer service representative at the agency.
stops.txt,stop_id,ID,Required,"Identifies a stop, station, or station entrance.

The term ""station entrance"" refers to both station entrances and station exits. Stops, stations or station entrances are collectively referred to as locations. Multiple routes may use the same stop."
stops.txt,stop_code,Text,Optional,Short text or a number that identifies the location for riders. These codes are often used in phone-based transit information systems or printed on signage to make it easier for riders to get information for a particular location. The stop_code can be the same as stop_id if it is public facing. This field should be left empty for locations without a code presented to riders.
stops.txt,stop_name,Text,Conditionally Required,"Name of the location. Use a name that people will understand in the local and tourist vernacular.

When the location is a boarding area (location_type=4), the stop_name should contains the name of the boarding area as displayed by the agency. It could be just one letter (like on some European intercity railway stations), or text like “Wheelchair boarding area” (NYC’s Subway) or “Head of short trains” (Paris’ RER).

Conditionally Required:
• Required for locations which are stops (location_type=0), stations (location_type=1) or entrances/exits (location_type=2).
• Optional for locations which are generic nodes (location_type=3) or boarding areas (location_type=4)."
stops.txt,tts_stop_name,Text,Optional,"Readable version of the stop_name. See ""Text-to-speech field"" in the Term Definitions for more."
stops.txt,stop_desc,Text,Optional,"Description of the location that provides useful, quality information. Do not simply duplicate the name of the location."
stops.txt,stop_lat,Latitude,Conditionally Required,"Latitude of the location.

For stops/platforms (location_type=0) and boarding area (location_type=4), the coordinates must be the ones of the bus pole — if exists — and otherwise of where the travelers are boarding the vehicle (on the sidewalk or the platform, and not on the roadway or the track where the vehicle stops).

Conditionally Required:
• Required for locations which are stops (location_type=0), stations (location_type=1) or entrances/exits (location_type=2).
• Optional for locations which are generic nodes (location_type=3) or boarding areas (location_type=4)."
stops.txt,stop_lon,Longitude,Conditionally Required,"Longitude of the location.

For stops/platforms (location_type=0) and boarding area (location_type=4), the coordinates must be the ones of the bus pole — if exists — and otherwise of where the travelers are boarding the vehicle (on the sidewalk or the platform, and not on the roadway or the track where the vehicle stops).

Conditionally Required:
• Required for locations which are stops (location_type=0), stations (location_type=1) or entrances/exits (location_type=2).
• Optional for locations which are generic nodes (location_type=3) or boarding areas (location_type=4)."
stops.txt,zone_id,ID,Conditionally Required,"Identifies the fare zone for a stop. This field is required if providing fare information using fare_rules.txt, otherwise it is optional. If this record represents a station or station entrance, the zone_id is ignored."
stops.txt,stop_url,URL,Optional,URL of a web page about the location. This should be different from the agency.agency_url and the routes.route_url field values.
stops.txt,location_type,Enum,Optional,"	Type of the location:
• 0 (or blank): Stop (or Platform). A location where passengers board or disembark from a transit vehicle. Is called a platform when defined within a parent_station.
• 1: Station. A physical structure or area that contains one or more platform.
• 2: Entrance/Exit. A location where passengers can enter or exit a station from the street. If an entrance/exit belongs to multiple stations, it can be linked by pathways to both, but the data provider must pick one of them as parent.
• 3: Generic Node. A location within a station, not matching any other location_type, which can be used to link together pathways define in pathways.txt.
• 4: Boarding Area. A specific location on a platform, where passengers can board and/or alight vehicles."
stops.txt,parent_station,ID referencing stops.stop_id,Conditionally Required,"Defines hierarchy between the different locations defined in stops.txt. It contains the ID of the parent location, as followed:
• Stop/platform (location_type=0): the parent_station field contains the ID of a station.
• Station (location_type=1): this field must be empty.
• Entrance/exit (location_type=2) or generic node (location_type=3): the parent_station field contains the ID of a station (location_type=1)
• Boarding Area (location_type=4): the parent_station field contains ID of a platform.

Conditionally Required:
• Required for locations which are entrances (location_type=2), generic nodes (location_type=3) or boarding areas (location_type=4).
• Optional for stops/platforms (location_type=0).
• Forbidden for stations (location_type=1)."
stops.txt,stop_timezone,Timezone,Optional,"Timezone of the location. If the location has a parent station, it inherits the parent station’s timezone instead of applying its own. Stations and parentless stops with empty stop_timezone inherit the timezone specified by agency.agency_timezone. If stop_timezone values are provided, the times in stop_times.txt should be entered as the time since midnight in the timezone specified by agency.agency_timezone. This ensures that the time values in a trip always increase over the course of a trip, regardless of which timezones the trip crosses."
stops.txt,wheelchair_boarding,Enum,Optional,"Indicates whether wheelchair boardings are possible from the location. Valid options are:

For parentless stops:
0 or empty - No accessibility information for the stop.
1 - Some vehicles at this stop can be boarded by a rider in a wheelchair.
2 - Wheelchair boarding is not possible at this stop.

For child stops:
0 or empty - Stop will inherit its wheelchair_boarding behavior from the parent station, if specified in the parent.
1 - There exists some accessible path from outside the station to the specific stop/platform.
2 - There exists no accessible path from outside the station to the specific stop/platform.

For station entrances/exits:
0 or empty - Station entrance will inherit its wheelchair_boarding behavior from the parent station, if specified for the parent.
1 - Station entrance is wheelchair accessible.
2 - No accessible path from station entrance to stops/platforms."
stops.txt,level_id,ID referencing levels.level_id,Optional,Level of the location. The same level can be used by multiple unlinked stations.
stops.txt,platform_code,Text,Optional,"Platform identifier for a platform stop (a stop belonging to a station). This should be just the platform identifier (eg. ""G"" or ""3""). Words like “platform” or ""track"" (or the feed’s language-specific equivalent) should not be included. This allows feed consumers to more easily internationalize and localize the platform identifier into other languages."
routes.txt,route_id,ID,Required,Identifies a route.
routes.txt,agency_id,ID referencing agency.agency_id,Conditionally required,"Agency for the specified route. This field is required when the dataset provides data for routes from more than one agency in agency.txt, otherwise it is optional."
routes.txt,route_short_name,Text,Conditionally required,"Short name of a route. This will often be a short, abstract identifier like ""32"", ""100X"", or ""Green"" that riders use to identify a route, but which doesn't give any indication of what places the route serves. Either route_short_name or route_long_name must be specified, or potentially both if appropriate."
routes.txt,route_long_name,Text,Conditionally required,"Full name of a route. This name is generally more descriptive than the route_short_name and often includes the route's destination or stop. Either route_short_name or route_long_name must be specified, or potentially both if appropriate."
routes.txt,route_desc,Text,Optional,"Description of a route that provides useful, quality information. Do not simply duplicate the name of the route.
Example: ""A"" trains operate between Inwood-207 St, Manhattan and Far Rockaway-Mott Avenue, Queens at all times. Also from about 6AM until about midnight, additional ""A"" trains operate between Inwood-207 St and Lefferts Boulevard (trains typically alternate between Lefferts Blvd and Far Rockaway)."
routes.txt,route_type,Enum,Required,"Indicates the type of transportation used on a route. Valid options are:

0 - Tram, Streetcar, Light rail. Any light rail or street level system within a metropolitan area.
1 - Subway, Metro. Any underground rail system within a metropolitan area.
2 - Rail. Used for intercity or long-distance travel.
3 - Bus. Used for short- and long-distance bus routes.
4 - Ferry. Used for short- and long-distance boat service.
5 - Cable tram. Used for street-level rail cars where the cable runs beneath the vehicle, e.g., cable car in San Francisco.
6 - Aerial lift, suspended cable car (e.g., gondola lift, aerial tramway). Cable transport where cabins, cars, gondolas or open chairs are suspended by means of one or more cables.
7 - Funicular. Any rail system designed for steep inclines.
11 - Trolleybus. Electric buses that draw power from overhead wires using poles.
12 - Monorail. Railway in which the track consists of a single rail or a beam."
routes.txt,route_url,URL,Optional,URL of a web page about the particular route. Should be different from the agency.agency_url value.
routes.txt,route_color,Color,Optional,Route color designation that matches public facing material. Defaults to white (FFFFFF) when omitted or left empty. The color difference between route_color and route_text_color should provide sufficient contrast when viewed on a black and white screen.
routes.txt,route_text_color,Color,Optional,Legible color to use for text drawn against a background of route_color. Defaults to black (000000) when omitted or left empty. The color difference between route_color and route_text_color should provide sufficient contrast when viewed on a black and white screen.
routes.txt,route_sort_order,Non-negative integer,Optional,Orders the routes in a way which is ideal for presentation to customers. Routes with smaller route_sort_order values should be displayed first.
routes.txt,continuous_pickup,Enum,Optional,"Indicates that the rider can board the transit vehicle at any point along the vehicle’s travel path as described by shapes.txt, on every trip of the route. Valid options are:

0 - Continuous stopping pickup.
1 or empty - No continuous stopping pickup.
2 - Must phone agency to arrange continuous stopping pickup.
3 - Must coordinate with driver to arrange continuous stopping pickup.

The continuous pickup behavior defined in routes.txt can be overridden in stop_times.txt."
routes.txt,continuous_drop_off,Enum,Optional,"Indicates that the rider can alight from the transit vehicle at any point along the vehicle’s travel path as described by shapes.txt, on every trip of the route. Valid options are:

0 - Continuous stopping drop off.
1 or empty - No continuous stopping drop off.
2 - Must phone agency to arrange continuous stopping drop off.
3 - Must coordinate with driver to arrange continuous stopping drop off.

The continuous drop-off behavior defined in routes.txt can be overridden in stop_times.txt."
trips.txt,route_id,ID referencing routes.route_id,Required,Identifies a route.
trips.txt,service_id,ID referencing calendar.service_id or calendar_dates.service_id,Required,Identifies a set of dates when service is available for one or more routes.
trips.txt,trip_id,ID,Required,Identifies a trip.
trips.txt,trip_headsign,Text,Optional,"Text that appears on signage identifying the trip's destination to riders. Use this field to distinguish between different patterns of service on the same route. If the headsign changes during a trip, trip_headsign can be overridden by specifying values for the stop_times.stop_headsign."
trips.txt,trip_short_name,Text,Optional,"Public facing text used to identify the trip to riders, for instance, to identify train numbers for commuter rail trips. If riders do not commonly rely on trip names, leave this field empty. A trip_short_name value, if provided, should uniquely identify a trip within a service day; it should not be used for destination names or limited/express designations."
trips.txt,direction_id,Enum,Optional,"Indicates the direction of travel for a trip. This field is not used in routing; it provides a way to separate trips by direction when publishing time tables. Valid options are:

0 - Travel in one direction (e.g. outbound travel).
1 - Travel in the opposite direction (e.g. inbound travel).
Example: The trip_headsign and direction_id fields could be used together to assign a name to travel in each direction for a set of trips. A trips.txt file could contain these records for use in time tables:
trip_id,...,trip_headsign,direction_id
1234,...,Airport,0
1505,...,Downtown,1"
trips.txt,block_id,ID,Optional,"Identifies the block to which the trip belongs. A block consists of a single trip or many sequential trips made using the same vehicle, defined by shared service days and block_id. A block_id can have trips with different service days, making distinct blocks. See the example below"
trips.txt,shape_id,ID referencing shapes.shape_id,Conditionally Required,"Identifies a geospatial shape describing the vehicle travel path for a trip.

Conditionally Required:
- Required if the trip has a continuous pickup or drop-off behavior defined either in routes.txt or in stop_times.txt.
- Optional otherwise."
trips.txt,wheelchair_accessible,Enum,Optional,"Indicates wheelchair accessibility. Valid options are:

0 or empty - No accessibility information for the trip.
1 - Vehicle being used on this particular trip can accommodate at least one rider in a wheelchair.
2 - No riders in wheelchairs can be accommodated on this trip."
trips.txt,bikes_allowed,Enum,Optional,"	Indicates whether bikes are allowed. Valid options are:

0 or empty - No bike information for the trip.
1 - Vehicle being used on this particular trip can accommodate at least one bicycle.
2 - No bicycles are allowed on this trip."
stop_times.txt,trip_id,ID referencing trips.trip_id,Required,Identifies a trip.
stop_times.txt,arrival_time,Time,Conditionally required,"Arrival time at a specific stop for a specific trip on a route. If there are not separate times for arrival and departure at a stop, enter the same value for arrival_time and departure_time. For times occurring after midnight on the service day, enter the time as a value greater than 24:00:00 in HH:MM:SS local time for the day on which the trip schedule begins.

Scheduled stops where the vehicle strictly adheres to the specified arrival and departure times are timepoints. If this stop is not a timepoint, it is recommended to provide an estimated or interpolated time. If this is not available, arrival_time can be left empty. Further, indicate that interpolated times are provided with timepoint=0. If interpolated times are indicated with timepoint=0, then time points must be indicated with timepoint=1. Provide arrival times for all stops that are time points. An arrival time must be specified for the first and the last stop in a trip."
stop_times.txt,departure_time,Time,Conditionally required,"Departure time from a specific stop for a specific trip on a route. For times occurring after midnight on the service day, enter the time as a value greater than 24:00:00 in HH:MM:SS local time for the day on which the trip schedule begins. If there are not separate times for arrival and departure at a stop, enter the same value for arrival_time and departure_time. See the arrival_time description for more details about using timepoints correctly.

The departure_time field should specify time values whenever possible, including non-binding estimated or interpolated times between timepoints."
stop_times.txt,stop_id,ID referencing stops.stop_id,Required,"Identifies the serviced stop. All stops serviced during a trip must have a record in stop_times.txt. Referenced locations must be stops, not stations or station entrances. A stop may be serviced multiple times in the same trip, and multiple trips and routes may service the same stop."
stop_times.txt,stop_sequence,Non-negative integer,Required,"Order of stops for a particular trip. The values must increase along the trip but do not need to be consecutive.
Example: The first location on the trip could have a stop_sequence=1, the second location on the trip could have a stop_sequence=23, the third location could have a stop_sequence=40, and so on."
stop_times.txt,stop_headsign,Text,Optional,"	Text that appears on signage identifying the trip's destination to riders. This field overrides the default trips.trip_headsign when the headsign changes between stops. If the headsign is displayed for an entire trip, use trips.trip_headsign instead.

A stop_headsign value specified for one stop_time does not apply to subsequent stop_times in the same trip. If you want to override the trip_headsign for multiple stop_times in the same trip, the stop_headsign value must be repeated in each stop_time row."
stop_times.txt,pickup_type,Enum,Optional,"Indicates pickup method. Valid options are:

0 or empty - Regularly scheduled pickup.
1 - No pickup available.
2 - Must phone agency to arrange pickup.
3 - Must coordinate with driver to arrange pickup."
stop_times.txt,drop_off_type,Enum,Optional,"Indicates drop off method. Valid options are:

0 or empty - Regularly scheduled drop off.
1 - No drop off available.
2 - Must phone agency to arrange drop off.
3 - Must coordinate with driver to arrange drop off."
stop_times.txt,continuous_pickup,Enum,Optional,"Indicates that the rider can board the transit vehicle at any point along the vehicle’s travel path as described by shapes.txt, from this stop_time to the next stop_time in the trip’s stop_sequence. Valid options are:

0 - Continuous stopping pickup.
1 or empty - No continuous stopping pickup.
2 - Must phone agency to arrange continuous stopping pickup.
3 - Must coordinate with driver to arrange continuous stopping pickup.

If this field is populated, it overrides any continuous pickup behavior defined in routes.txt. If this field is empty, the stop_time inherits any continuous pickup behavior defined in routes.txt."
stop_times.txt,continuous_drop_off,Enum,Optional,"Indicates that the rider can alight from the transit vehicle at any point along the vehicle’s travel path as described by shapes.txt, from this stop_time to the next stop_time in the trip’s stop_sequence. Valid options are:

0 - Continuous stopping drop off.
1 or empty - No continuous stopping drop off.
2 - Must phone agency to arrange continuous stopping drop off.
3 - Must coordinate with driver to arrange continuous stopping drop off.

If this field is populated, it overrides any continuous drop-off behavior defined in routes.txt. If this field is empty, the stop_time inherits any continuous drop-off behavior defined in routes.txt."
stop_times.txt,shape_dist_traveled,Non-negative float,Optional,"	Actual distance traveled along the associated shape, from the first stop to the stop specified in this record. This field specifies how much of the shape to draw between any two stops during a trip. Must be in the same units used in shapes.txt. Values used for shape_dist_traveled must increase along with stop_sequence; they cannot be used to show reverse travel along a route.
Example: If a bus travels a distance of 5.25 kilometers from the start of the shape to the stop,shape_dist_traveled=5.25."
stop_times.txt,timepoint,Enum,Optional,"Indicates if arrival and departure times for a stop are strictly adhered to by the vehicle or if they are instead approximate and/or interpolated times. This field allows a GTFS producer to provide interpolated stop-times, while indicating that the times are approximate. Valid options are:

0 - Times are considered approximate.
1 or empty - Times are considered exact."
calendar.txt,ervice_id,ID,Required,Uniquely identifies a set of dates when service is available for one or more routes. Each service_id value can appear at most once in a calendar.txt file.
calendar.txt,monday,Enum,Required,"Indicates whether the service operates on all Mondays in the date range specified by the start_date and end_date fields. Note that exceptions for particular dates may be listed in calendar_dates.txt. Valid options are:

1 - Service is available for all Mondays in the date range.
0 - Service is not available for Mondays in the date range."
calendar.txt,tuesday,Enum,Required,Functions in the same way as monday except applies to Tuesdays
calendar.txt,wednesday,Enum,Required,Functions in the same way as monday except applies to Wednesdays
calendar.txt,thursday,Enum,Required,Functions in the same way as monday except applies to Thursdays
calendar.txt,friday,Enum,Required,Functions in the same way as monday except applies to Fridays
calendar.txt,saturday,Enum,Required,Functions in the same way as monday except applies to Saturdays.
calendar.txt,sunday,Enum,Required,Functions in the same way as monday except applies to Sundays.
calendar.txt,start_date,Date,Required,Start service day for the service interval.
calendar.txt,end_date,Date,Required,End service day for the service interval. This service day is included in the interval.
calendar_dates.txt,service_id,ID referencing calendar.service_id or ID,Required,"Identifies a set of dates when a service exception occurs for one or more routes. Each (service_id, date) pair can only appear once in calendar_dates.txt if using calendar.txt and calendar_dates.txt in conjunction. If a service_id value appears in both calendar.txt and calendar_dates.txt, the information in calendar_dates.txt modifies the service information specified in calendar.txt."
calendar_dates.txt,date,Date,Required,Date when service exception occurs.
calendar_dates.txt,exception_type,Enum,Required,"Indicates whether service is available on the date specified in the date field. Valid options are:

1 - Service has been added for the specified date.
2 - Service has been removed for the specified date.
Example: Suppose a route has one set of trips available on holidays and another set of trips available on all other days. One service_id could correspond to the regular service schedule and another service_id could correspond to the holiday schedule. For a particular holiday, the calendar_dates.txt file could be used to add the holiday to the holiday service_id and to remove the holiday from the regular service_id schedule."
fare_attributes.txt,fare_id,ID,Required,Identifies a fare class.
fare_attributes.txt,price,Non-negative float,Required,"Fare price, in the unit specified by currency_type."
fare_attributes.txt,currency_type,Currency code,Required,Currency used to pay the fare.
fare_attributes.txt,payment_method,Enum,Required,"Indicates when the fare must be paid. Valid options are:

0 - Fare is paid on board.
1 - Fare must be paid before boarding."
fare_attributes.txt,transfers,Enum,Required,"	Indicates the number of transfers permitted on this fare. The fact that this field can be left empty is an exception to the requirement that a Required field must not be empty. Valid options are:

0 - No transfers permitted on this fare.
1 - Riders may transfer once.
2 - Riders may transfer twice.
empty - Unlimited transfers are permitted."
fare_attributes.txt,agency_id,ID referencing agency.agency_id,Conditionally Required,"Identifies the relevant agency for a fare. This field is required for datasets with multiple agencies defined in agency.txt, otherwise it is optional."
fare_attributes.txt,transfer_duration,Non-negative integer,Optional,Length of time in seconds before a transfer expires. When transfers=0 this field can be used to indicate how long a ticket is valid for or it can can be left empty.
fare_rules.txt,fare_id,ID referencing fare_attributes.fare_id,Required,Identifies a fare class.
fare_rules.txt,route_id,ID referencing routes.route_id,Optional,"Identifies a route associated with the fare class. If several routes with the same fare attributes exist, create a record in fare_rules.txt for each route.
Example: If fare class ""b"" is valid on route ""TSW"" and ""TSE"", the fare_rules.txt file would contain these records for the fare class:
fare_id,route_id
b,TSW
b,TSE"
fare_rules.txt,origin_id,ID referencing stops.zone_id,Optional,"Identifies an origin zone. If a fare class has multiple origin zones, create a record in fare_rules.txt for each origin_id.
Example: If fare class ""b"" is valid for all travel originating from either zone ""2"" or zone ""8"", the fare_rules.txt file would contain these records for the fare class:
fare_id,...,origin_id
b,...,2
b,...,8"
fare_rules.txt,destination_id,ID referencing stops.zone_id,Optional,"dentifies a destination zone. If a fare class has multiple destination zones, create a record in fare_rules.txt for each destination_id.
Example: The origin_id and destination_id fields could be used together to specify that fare class ""b"" is valid for travel between zones 3 and 4, and for travel between zones 3 and 5, the fare_rules.txt file would contain these records for the fare class:
fare_id,...,origin_id,destination_id
b,...,3,4
b,...,3,5"
fare_rules.txt,contains_id,ID referencing stops.zone_id,Optional,"Identifies the zones that a rider will enter while using a given fare class. Used in some systems to calculate correct fare class.
Example: If fare class ""c"" is associated with all travel on the GRT route that passes through zones 5, 6, and 7 the fare_rules.txt would contain these records:
fare_id,route_id,...,contains_id
c,GRT,...,5
c,GRT,...,6
c,GRT,...,7
Because all contains_id zones must be matched for the fare to apply, an itinerary that passes through zones 5 and 6 but not zone 7 would not have fare class ""c"". For more detail, see https://code.google.com/p/googletransitdatafeed/wiki/FareExamples in the GoogleTransitDataFeed project wiki."
shapes.txt,shape_id,ID,Required,Identifies a shape.
shapes.txt,shape_pt_lat,Latitude,Required,Latitude of a shape point. Each record in shapes.txt represents a shape point used to define the shape.
shapes.txt,shape_pt_lon,Longitude,Required,Longitude of a shape point.
shapes.txt,shape_pt_sequence,Non-negative integer,Required,"Sequence in which the shape points connect to form the shape. Values must increase along the trip but do not need to be consecutive.
Example: If the shape ""A_shp"" has three points in its definition, the shapes.txt file might contain these records to define the shape:
shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence
A_shp,37.61956,-122.48161,0
A_shp,37.64430,-122.41070,6
A_shp,37.65863,-122.30839,11"
shapes.txt,shape_dist_traveled,Non-negative float,Optional,"Actual distance traveled along the shape from the first shape point to the point specified in this record. Used by trip planners to show the correct portion of the shape on a map. Values must increase along with shape_pt_sequence; they cannot be used to show reverse travel along a route. Distance units must be consistent with those used in stop_times.txt.
Example: If a bus travels along the three points defined above for A_shp, the additional shape_dist_traveled values (shown here in kilometers) would look like this:
shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence,shape_dist_traveled
A_shp,37.61956,-122.48161,0,0
A_shp,37.64430,-122.41070,6,6.8310
A_shp,37.65863,-122.30839,11,15.8765"
frequencies.txt,trip_id,ID referencing trips.trip_id,Required,Identifies a trip to which the specified headway of service applies.
frequencies.txt,start_time,Time,Required,Time at which the first vehicle departs from the first stop of the trip with the specified headway.
frequencies.txt,end_time,Time,Required,Time at which service changes to a different headway (or ceases) at the first stop in the trip.
frequencies.txt,headway_secs,Non-negative integer,Required,"Time, in seconds, between departures from the same stop (headway) for the trip, during the time interval specified by start_time and end_time. Multiple headways for the same trip are allowed, but may not overlap. New headways may start at the exact time the previous headway ends."
frequencies.txt,exact_times,Enum,Optional,"	Indicates the type of service for a trip. See the file description for more information. Valid options are:

0 or empty - Frequency-based trips.
1 - Schedule-based trips with the exact same headway throughout the day. In this case the end_time value must be greater than the last desired trip start_time but less than the last desired trip start_time + headway_secs."
transfers.txt,from_stop_id,ID referencing stops.stop_id,Required,"Identifies a stop or station where a connection between routes begins. If this field refers to a station, the transfer rule applies to all its child stops."
transfers.txt,to_stop_id,ID referencing stops.stop_id,Required,"Identifies a stop or station where a connection between routes ends. If this field refers to a station, the transfer rule applies to all child stops."
transfers.txt,transfer_type,Enum,Required,"Indicates the type of connection for the specified (from_stop_id, to_stop_id) pair. Valid options are:

0 or empty - Recommended transfer point between routes.
1 - Timed transfer point between two routes. The departing vehicle is expected to wait for the arriving one and leave sufficient time for a rider to transfer between routes.
2 - Transfer requires a minimum amount of time between arrival and departure to ensure a connection. The time required to transfer is specified by min_transfer_time.
3 - Transfers are not possible between routes at the location."
transfers.txt,min_transfer_time,Non-negative integer,Optional,"Amount of time, in seconds, that must be available to permit a transfer between routes at the specified stops. The min_transfer_time should be sufficient to permit a typical rider to move between the two stops, including buffer time to allow for schedule variance on each route."
pathways.txt,pathway_id,ID,Required,"The pathway_id field contains an ID that uniquely identifies the pathway. The pathway_id is used by systems as an internal identifier of this record (e.g., primary key in database), and therefore the pathway_id must be dataset unique.
Different pathways can go from the same from_stop_id to the same to_stop_id. For example, this happens when two escalators are side by side in opposite direction, or when a stair is nearby and elevator and both go from the same place to the same place."
pathways.txt,from_stop_id,ID referencing stops.stop_id,Required,"Location at which the pathway begins. It contains a stop_id that identifies a platform, entrance/exit, generic node or boarding area from the stops.txt file."
pathways.txt,to_stop_id,ID referencing stops.stop_id,Required,"Location at which the pathway ends. It contains a stop_id that identifies a platform, entrance/exit, generic node or boarding area from the stops.txt file."
pathways.txt,pathway_mode,Enum,Required,"Type of pathway between the specified (from_stop_id, to_stop_id) pair. Valid values for this field are:
• 1: walkway
• 2: stairs
• 3: moving sidewalk/travelator
• 4: escalator
• 5: elevator
• 6: fare gate (or payment gate): A pathway that crosses into an area of the station where a proof of payment is required (usually via a physical payment gate).
Fare gates may either separate paid areas of the station from unpaid ones, or separate different payment areas within the same station from each other. This information can be used to avoid routing passengers through stations using shortcuts that would require passengers to make unnecessary payments, like directing a passenger to walk through a subway platform to reach a busway.
• 7: exit gate: Indicates a pathway exiting an area where proof-of-payment is required into an area where proof-of-payment is no longer required."
pathways.txt,is_bidirectional,Enum,Required,"Indicates in which direction the pathway can be used:
• 0: Unidirectional pathway, it can only be used from from_stop_id to to_stop_id.
• 1: Bidirectional pathway, it can be used in the two directions.

Fare gates (pathway_mode=6) and exit gates (pathway_mode=7) cannot be bidirectional."
pathways.txt,length,Non-negative Float,Optional,"Horizontal length in meters of the pathway from the origin location (defined in from_stop_id) to the destination location (defined in to_stop_id).

This field is recommended for walkways (pathway_mode=1), fare gates (pathway_mode=6) and exit gates (pathway_mode=7)."
pathways.txt,traversal_time,Positive Integer,Optional,"	Average time in seconds needed to walk through the pathway from the origin location (defined in from_stop_id) to the destination location (defined in to_stop_id).

This field is recommended for moving sidewalks (pathway_mode=3), escalators (pathway_mode=4) and elevator (pathway_mode=5)."
pathways.txt,stair_count,Non-null Integer,Optional,"Number of stairs of the pathway.

Best Practices: one could use the approximation of 1 floor = 15 stairs to generate approximative values.

A positive stair_count implies that the rider walk up from from_stop_id to to_stop_id. And a negative stair_count implies that the rider walk down from from_stop_id to to_stop_id.

This field is recommended for stairs (pathway_mode=2)."
pathways.txt,max_slope,Float,Optional,"Maximum slope ratio of the pathway. Valid values for this field are:
• 0 or (empty): no slope.
• A float: slope ratio of the pathway, positive for upwards, negative for downwards.

This field should be used only with walkways (pathway_mode=1) and moving sidewalks (pathway_mode=3).

Example: In the US, 0.083 (also written 8.3%) is the maximum slope ratio for hand-propelled wheelchair, which mean an increase of 0.083m (so 8.3cm) for each 1m."
pathways.txt,min_width,Positive Float,Optional,"Minimum width of the pathway in meters.

This field is highly recommended if the minimum width is less than 1 meter."
pathways.txt,signposted_as,Text,Optional,"String of text from physical signage visible to transit riders. The string can be used to provide text directions to users, such as 'follow signs to '. The language text should appear in this field exactly how it is printed on the signs.

When the physical signage is multilingual, this field may be populated and translated following the example of stops.stop_name in the field definition of feed_info.feed_lang."
pathways.txt,reversed_signposted_as,Text,Optional,"Same than the signposted_as field, but when the pathways is used backward, i.e. from the to_stop_id to the from_stop_id."
levels.txt,level_id,ID,Required,Id of the level that can be referenced from stops.txt.
levels.txt,level_index,Float,Required,"Numeric index of the level that indicates relative position of this level in relation to other levels (levels with higher indices are assumed to be located above levels with lower indices).

Ground level should have index 0, with levels above ground indicated by positive indices and levels below ground by negative indices."
levels.txt,level_name,Text,Optional,Optional name of the level (that matches level lettering/numbering used inside the building or the station). Is useful for elevator routing (e.g. “take the elevator to level “Mezzanine” or “Platforms” or “-1”).
translations.txt,table_name,Enum,Required,"Defines the table that contains the field to be translated. Allowed values are: agency, stops, routes, trips, stop_times, pathways, levels, feed_info and attributions (do not include the .txt file extension). If a table with a new file name is added by another proposal in the future, the table name is the name of the filename without the .txt file extension."
translations.txt,field_name,Text,Required,"Name of the field to be translated. Fields with type Text can be translated, fields with type URL, Email and Phone number can also be “translated” to provide resources in the correct language. Fields with other types should not be translated."
translations.txt,language,Language code,Required,"Language of translation.

If the language is the same as in feed_info.feed_lang, the original value of the field will be assumed to be the default value to use in languages without specific translations (if default_lang doesn't specify otherwise).

Example: In Switzerland, a city in an officially bilingual canton is officially called “Biel/Bienne”, but would simply be called “Bienne” in French and “Biel” in German."
translations.txt,translation,Text or URL or Email or Phone number,Required,Translated value.
translations.txt,record_id,ID,Conditionally Required,"Defines the record that corresponds to the field to be translated. The value in record_id should be a main ID of the table, as defined below:
• agency_id for agency.txt;
• stop_id for stops.txt;
• route_id for routes.txt;
• trip_id for trips.txt;
• trip_id for stop_times.txt;
• pathway_id for pathways.txt;
• level_id for levels.txt;
• attribution_id for attribution.txt.

No field should be translated in the other tables. However producers sometimes add extra fields that are outside the official specification and these unofficial fields may need to be translated. Below is the recommended way to use record_id for those tables:
• service_id for calendar.txt;
• service_id for calendar_dates.txt;
• fare_id for fare_attributes.txt;
• fare_id for fare_rules.txt;
• shape_id for shapes.txt;
• trip_id for frequencies.txt;
• from_stop_id for transfers.txt.

Conditionally Required:
- forbidden if table_name is feed_info;
- forbidden if field_value is defined;
- required if field_value is empty."
translations.txt,record_sub_id,ID,Conditionally Required,"Helps the record that contains the field to be translated when the table doesn’t have a unique ID. Therefore, the value in record_sub_id is the secondary ID of the table, as defined by the table below:
• None for agency.txt;
• None for stops.txt;
• None for routes.txt;
• None for trips.txt;
• stop_sequence for stop_times.txt;
• None for pathways.txt;
• None for levels.txt;
• None for attributions.txt.

No field should be translated in the other tables. However producers sometimes add extra fields that are outside the official specification and these unofficial fields may need to be translated. Below is the recommended way to use record_sub_id for those tables:
• None for calendar.txt;
• date for calendar_dates.txt;
• None for fare_attributes.txt;
• route_id for fare_rules.txt;
• None for shapes.txt;
• start_time for frequencies.txt;
• to_stop_id for transfers.txt.

Conditionally Required:
- forbidden if table_name is feed_info;
- forbidden if field_value is defined;
- required if table_name=stop_times and record_id is defined."
translations.txt,field_value,Text or URL or Email or Phone number,Conditionally Required,"Instead of defining which record should be translated by using record_id and record_sub_id, this field can be used to define the value which should be translated. When used, the translation will be applied when the fields identified by table_name and field_name contains the exact same value defined in field_value.

The field must have exactly the value defined in field_value. If only a subset of the value matches field_value, the translation won’t be applied.

If two translation rules match the same record (one with field_value, and the other one with record_id), then the rule with record_id is the one which should be used.

Conditionally Required:
- forbidden if table_name is feed_info;
- forbidden if record_id is defined;
- required if record_id is empty."
feed_info.txt,feed_publisher_name,Text,Required,Full name of the organization that publishes the dataset. This may be the same as one of the agency.agency_name values.
feed_info.txt,feed_publisher_url,URL,Required,URL of the dataset publishing organization's website. This may be the same as one of the agency.agency_url values.
feed_info.txt,feed_lang,Language code,Required,"Default language used for the text in this dataset. This setting helps GTFS consumers choose capitalization rules and other language-specific settings for the dataset. The file translations.txt can be used if the text needs to be translated into languages other than the default one.

The default language may be multilingual for datasets with the original text in multiple languages. In such cases, the feed_lang field should contain the language code mul defined by the norm ISO 639-2. The best practice here would be to provide, in translations.txt, a translation for each language used throughout the dataset. If all the original text in the dataset is in the same language, then mul should not be used.
Example: Consider a dataset from a multilingual country like Switzerland, with the original stops.stop_name field populated with stop names in different languages. Each stop name is written according to the dominant language in that stop’s geographic location, e.g. Genève for the French-speaking city of Geneva, Zürich for the German-speaking city of Zurich, and Biel/Bienne for the bilingual city of Biel/Bienne. The dataset feed_lang should be mul and translations would be provided in translations.txt, in German: Genf, Zürich and Biel; in French: Genève, Zurich and Bienne; in Italian: Ginevra, Zurigo and Bienna; and in English: Geneva, Zurich and Biel/Bienne."
feed_info.txt,default_lang,Language code,Optional,Defines the language that should be used when the data consumer doesn’t know the language of the rider. It will often be en (English).
feed_info.txt,feed_start_date,Date,Optional,"The dataset provides complete and reliable schedule information for service in the period from the beginning of the feed_start_date day to the end of the feed_end_date day. Both days can be left empty if unavailable. The feed_end_date date must not precede the feed_start_date date if both are given. Dataset providers are encouraged to give schedule data outside this period to advise of likely future service, but dataset consumers should treat it mindful of its non-authoritative status. If feed_start_date or feed_end_date extend beyond the active calendar dates defined in calendar.txt and calendar_dates.txt, the dataset is making an explicit assertion that there is no service for dates within the feed_start_date or feed_end_date range but not included in the active calendar dates."
feed_info.txt,feed_end_date,Date,Optional,(see feed_start_date)
feed_info.txt,feed_version,Text,Optional,String that indicates the current version of their GTFS dataset. GTFS-consuming applications can display this value to help dataset publishers determine whether the latest dataset has been incorporated.
feed_info.txt,feed_contact_email,Email,Optional,Email address for communication regarding the GTFS dataset and data publishing practices. feed_contact_email is a technical contact for GTFS-consuming applications. Provide customer service contact information through agency.txt.
feed_info.txt,feed_contact_url,URL,Optional,"URL for contact information, a web-form, support desk, or other tools for communication regarding the GTFS dataset and data publishing practices. feed_contact_url is a technical contact for GTFS-consuming applications. Provide customer service contact information through agency.txt."
attributions.txt,Field Name,Type,Required,Description
attributions.txt,attribution_id,ID,Optional,Identifies an attribution for the dataset or a subset of it. This is mostly useful for translations.
attributions.txt,agency_id,ID referencing agency.agency_id,Optional,"Agency to which the attribution applies.

If one agency_id, route_id, or trip_id attribution is defined, the other ones must be empty. If none of them is specified, the attribution will apply to the whole dataset."
attributions.txt,route_id,ID referencing routes.route_id,Optional,Functions in the same way as agency_id except the attribution applies to a route. Multiple attributions can apply to the same route.
attributions.txt,trip_id,ID referencing trips.trip_id,Optional,Functions in the same way as agency_id except the attribution applies to a trip. Multiple attributions can apply to the same trip.
attributions.txt,organization_name,Text,Required,Name of the organization that the dataset is attributed to.
attributions.txt,is_producer,Enum,Optional,"The role of the organization is producer. Valid options are:

0 or empty - Organization doesn’t have this role.
1 - Organization does have this role.

At least one of the fields is_producer, is_operator, or is_authority should be set at 1."
attributions.txt,is_operator,Enum,Optional,Functions in the same way as is_producer except the role of the organization is operator.
attributions.txt,is_authority,Enum,Optional,Functions in the same way as is_producer except the role of the organization is authority.
attributions.txt,attribution_url,URL,Optional,URL of the organization.
attributions.txt,attribution_email,Email,Optional,Email of the organization.
attributions.txt,attribution_phone,Phone number,Optional,Phone number of the organization.
