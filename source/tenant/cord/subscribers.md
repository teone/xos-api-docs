FORMAT: 1A

# XOS

# Group Subscribers

Resource related to the CORD Subscribers.

## Subscribers Collection [/api/tenant/cord/subscriber/]

### List All Subscribers [GET]

+ Response 200 (application/json)

        [
            {
                "humanReadableName": "cordSubscriber-1", 
                "id": 1, 
                "service_specific_id": "123", 
                "features": {
                    "cdn": false, 
                    "uplink_speed": 1000000000, 
                    "downlink_speed": 1000000000, 
                    "uverse": true, 
                    "status": "enabled"
                }
            }
        ]

## Subscriber Detail [/api/tenant/cord/subscriber/{subscriber_id}/]

+ Parameters
    + subscriber_id: 1 (number) - ID of the Subscriber in the form of an integer

### View a Subscriber Detail [GET]

+ Response 200 (application/json)
 
        {
            "humanReadableName": "cordSubscriber-1", 
            "id": 1, 
            "service_specific_id": "123", 
            "features": {
                "cdn": false, 
                "uplink_speed": 1000000000, 
                "downlink_speed": 1000000000, 
                "uverse": true, 
                "status": "enabled"
            }
        }

### Delete a Subscriber [DELETE]

+ Response 204

## Subscriber features [/api/tenant/cord/subscriber/{subscriber_id}/features/]

+ Parameters
    + subscriber_id: 1 (number) - ID of the Subscriber in the form of an integer

### View a Subscriber Features Detail [GET]

+ Response 200 (application/json)

        {
            "cdn": false, 
            "uplink_speed": 1000000000, 
            "downlink_speed": 1000000000, 
            "uverse": true, 
            "status": "enabled"
        }

### Subscriber features uplink_speed [/api/tenant/cord/subscriber/{subscriber_id}/features/uplink_speed/]

+ Parameters
    + subscriber_id: 1 (number) - ID of the Subscriber in the form of an integer

#### Read Subscriber uplink_speed [GET]

+ Response 200 (application/json)

        {
            "uplink_speed": 1000000000
        }

#### Update Subscriber uplink_speed [PUT]

This request will set the uplink_speed to a new value for the designated subscriber

+ Request 200 (application/json)

        {
            "uplink_speed": 1000000000
        }

+ Response 200 (application/json)

        {
            "uplink_speed": 1000000000
        }
