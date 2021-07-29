# LogFly  
a simple log tool for python.  

## How to  
### import  
    import logfly  
### use  
    write_log('name', 'where', 'info', "message.")  

## Description  
    name: (any str) logfile name, you can use diffrent string to create diffrent logfile.  
    where: ('CLI', 'fileCLI', 'file') position where log appear.  
            fileCLI means log will appear in command line window and log file.  
            CLI means log will only appear in command line window.  
            file means log will only appear in logfile.  
    info: (any str) custom log level, will upper and wrap with '[]'.  
    message: (any str) log message.  

## Example:  
### code
    write_log('Doctor Who', 'CLI', 'info', "this is Doctor's log, only in CLI.")  
#### in CLI  
    2021-07-29 20:39:07 [INFO] this is Doctor's log, only in CLI.  
#### in file  
    None  

### code  
    write_log('Doctor Who', 'fileCLI', 'info', "this is Doctor's log, in file and CLI.")  
#### in CLI  
    2021-07-29 20:39:07 [INFO] this is Doctor's log, in file and CLI.  
#### in file (Doctor Who-2021-07-29.log)  
    2021-07-29 20:39:07 [INFO] this is Doctor's log, in file and CLI.  

### code  
    write_log('Doctor Who', 'file', 'info', "this is Doctor's log, in file and CLI.")  
#### in CLI  
    None  
#### in file (Doctor Who-2021-07-29.log)  
    2021-07-29 20:40:03 [INFO] this is Doctor's log, only in file.  