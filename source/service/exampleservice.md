# Group Example

## Example Services Collection [/api/service/exampleservice/]

This is the example service documentation, remember that this service should be enabled following this guide: http://guide.xosproject.org/devguide/exampleservice/

### List all Example Services [GET]

+ Response 200 (application/json)

        [
            {
                "humanReadableName": "MyExample",
                "id": 1,
                "service_message": "This is the test message"
            }
        ]