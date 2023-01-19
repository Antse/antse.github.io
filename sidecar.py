# Nomad workload diagram
from diagrams import Cluster, Diagram
from diagrams.onprem.monitoring import Datadog
from diagrams.onprem.compute import Nomad
from diagrams.generic.storage import Storage

with Diagram("Datadog Shipping with a sidecar task", show=False):
    ddog = Datadog("eu.datadog.hq")

    with Cluster("Nomad Cluster"):
        with Cluster("group-1"):
            task1 = Nomad("app-1 container")
            ddogtask2 = Nomad("Datadog container")
            store1 = Storage("allocation storage")
        with Cluster("group-2"):
            task3 = Nomad("app-2 container")
            ddogtask4 = Nomad("Datadog container")
            store2 = Storage("allocation storage")

    store1 << task1
    store2 << task3
    store1 << ddogtask2
    store2 << ddogtask4
    ddogtask2 >> ddog
    ddogtask4 >> ddog
