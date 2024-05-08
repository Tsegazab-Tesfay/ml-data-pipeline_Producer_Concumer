# ml-data-pipeline

1. Understand the flow from device to the mongodb
2. The bigger picture is:
    * Sensor -> Producer(Python script) -> KAFKA -> Consumer(Python script)

3. More detials picture:
    * PRODUCER PART [File(datafrma) -> object -> dictionary -> Json serelizer]
    * -> Kafka
    * CONSUMER PART [Json deserelizer -> Dictionary -> Object -> Mongodb -> Local(for analyzing+otherdoing data)]

#### Note:
* In reality, the producer (producer_main) and all other code would be in the IoT device.
And the consumer (consumer) should be in another project.

* In general, both the producer and consumer should not be in a single project. These will be in two different projects.
