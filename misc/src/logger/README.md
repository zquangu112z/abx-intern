## The most commonly used classes defined in the logging module are the following:

* **Logger**: This is the class whose objects will be used in the application code directly to call the functions.

* **[LogRecord](https://docs.python.org/3/library/logging.html#logging.LogRecord)**: Loggers automatically create LogRecord objects that have all the information related to the event being logged, like the name of the logger, the function, the line number, the message, and more.

* **[Handler](https://docs.python.org/3/library/logging.html#logging.Handler)**: Handlers send the LogRecord to the required output destination, like the console or a file. Handler is a base for subclasses like StreamHandler, FileHandler, SMTPHandler, HTTPHandler, and more. These subclasses send the logging outputs to corresponding destinations, like sys.stdout or a disk file.

* **[Formatter](https://docs.python.org/3/library/logging.html#logrecord-attributes)**: This is where you specify the format of the output by specifying a string format that lists out the attributes that the output should contain.

## Calling log flow

```pseudo
if loglevel >= self.level:
    for handler in self.handlers:
        handler(loglevel, message)
```

And in each handler:
```
if loglevel >= self.level:
    # do something
```