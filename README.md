# logfly 0.7  
### a simple log tool by python  

## position  
log will create in ./logs/folder_name/[date] folder.

## How to  
### import  
    import logfly  
### use  
    logfly.write_log('name', 'where', 'info', 'message', mode='add', folder_name='logflys')  

## Description  
    name: (any str) logfile name, you can use diffrent string to create diffrent logfile.  
    where: ('CLI', 'fileCLI', 'file') position where log appear.  
            fileCLI means log will appear in command line window and log file.  
            CLI means log will only appear in command line window.  
            file means log will only appear in logfile.  
    info: (any str) custom log level, will upper and wrap with '[]'.  
    message: (any str) log message.  
    mode: ('add', 'new') default is 'add', means log will add in same day.  
            'new' means logfile will create when program every once.
    folder_name: (any str) logfly folder name, default is logflys.  

## Example:  

### both file and CLI code  
    logfly.write_log('Doctor Who', 'fileCLI', 'info', "this is Doctor's log, in file and CLI.")  
#### in CLI  
    2021-07-29 20:39:07 [INFO] this is Doctor's log, in file and CLI.  
#### in file (/logs/logflys/Doctor Who-2021-07-29.log)  
    2021-07-29 20:39:07 [INFO] this is Doctor's log, in file and CLI.  
  
### only in CLI code
    logfly.write_log('Doctor Who', 'CLI', 'info', "this is Doctor's log, only in CLI.")  
#### in CLI  
    2021-07-29 20:39:07 [INFO] this is Doctor's log, only in CLI.  
#### in file  
    None

### only in file code  
    logfly.write_log('Doctor Who', 'file', 'info', "this is Doctor's log, in file and CLI.")  
#### in CLI  
    None  
#### in file (/logs/logflys/Doctor Who-2021-07-29.log)  
    2021-07-29 20:40:03 [INFO] this is Doctor's log, in file and CLI

#### mode arg:
    logfly.write_log('Doctor Who', 'file', 'info', "this is Doctor's log, in file and CLI.", mode='new')
#### in CLI:
    2021-07-29 20:40:03 [INFO] this is Doctor's log, only in file.
#### infile(/logs/logflys/2021-08-01/Doctor Who-20210801165807.log):  
#### p.s.  log will name in date + time  

    2021-07-29 20:40:03 [INFO] this is Doctor's log, in file and CLI  

#### folder_name arg:
    logfly.write_log('Doctor Who', 'file', 'info', "this is death's log, in file and CLI.", folder_name="death")
#### in CLI:
    2021-07-29 20:40:03 [INFO] tthis is death's log, in file and CLI
#### infile(/logs/death/2021-08-01/death-20210801165807.log):  
#### p.s.  log will name in date + time  

    2021-07-29 20:40:03 [INFO] this is death's log, in file and CLI