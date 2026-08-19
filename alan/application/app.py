class Application:
    """
    Alan lifecycle manager, responsible for:
    - loading configuration and initializing components;
    - starting program execution;
    - shutting down safely all the components.
    """

    def __init__(self):
        self.core = None
        self.config = None

    def initialize(self):
        """
        Initialize Alan environment.

        Responsibilities
        - load configuration;
        - create core;
        - create services;
        - prepare tools.
        """

        print("Status: Initializing")

    def start(self):
        """
        Start execution.

        Responsibilities
        - launch core;
        - launch application loop.
        """

        print("Status: Running")

    def shutdown(self):
        """
        Terminate Alan execution.

        Responsibilities
        - stop core;
        - save memory;
        - close resources.
        """

        print("Status: Shutting down")