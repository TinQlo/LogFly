# logfly  1.8  
### a simple log tool by python  

## position  
log will create in ./logs/[folder_name]/[date] folder.  
if use hidden, log will also appear in user/.1o9f1y folder  

## How to  
### import  
    import logfly  
### use1  
    logfly.write_log('name', 'where', 'info', 'message', mode='add', folder_name='logflys', hidden='no', color='yes', str_message='yes')  

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
    folder_name: (any str) custom logfly folder name, default is 'logflys'.  
    hidden: ('yes', 'no') default is 'no', means logfile will save a copy in user/.1o9f1y folder  
    color: ('yes', 'no') default is 'yes', means log will with color.  
    str_message: ('yes', 'no') default is 'yes', means log will print message with str()  

###use2  
    logfly.create_file(pathfile='', filenname='')  

##Description  
    pathfile is the file path that you want to create, must fill with //  
    filenname is the file name that you want to create, must is with *.*  

## Example:  

### both file and CLI code  
    logfly.write_log('Doctor Who', 'fileCLI', 'info', "this is Doctor's log, in file and CLI.")  
#### in CLI  
    2021-07-29 20:39:07 [INFO] this is Doctor's log, in file and CLI.  
#### in file (logs/logflys/[date]/Doctor Who-2021-07-29.log)  
    2021-07-29 20:39:07 [INFO] this is Doctor's log, in file and CLI.  
  
### only in CLI code
    logfly.write_log('Doctor Who', 'CLI', 'info', "this is Doctor's log, only in CLI.")  
#### in CLI  
    2021-07-29 20:39:07 [INFO] this is Doctor's log, only in CLI.  
#### in file  
    None

### only in file code  
    logfly.write_log('Doctor Who', 'file', 'info', "this is Doctor's log, only in file.")  
#### in CLI  
    None  
#### in file (logs/logflys/[date]/Doctor Who-2021-07-29.log)  
    2021-07-29 20:40:03 [INFO] this is Doctor's log, only in file.  

#### mode arg:
    logfly.write_log('Doctor Who', 'file', 'info', "this is Doctor's log, only in file.", mode='new')
#### in CLI:
    2021-07-29 20:40:03 [INFO] this is Doctor's log, only in file.
#### infile(logs//logflys[date]/Doctor Who-20210801165807.log):  
#### p.s.  log will name in date + time  

    2021-07-29 20:40:03 [INFO] this is Doctor's log, only in file.  

#### folder arg:
    write_log('Death Stranding', 'fileCLI', 'info', "this is Death Stranding's log, in file and CLI.", mode='add',folder_name='games')
#### in CLI:
    2021-11-10 21:27:55 [INFO] this is Death Stranding's log, in file and CLI.
#### infile(logs/games/[date]/Death Stranding-20210801165807.log):

    2021-11-10 21:27:55 [INFO] this is Death Stranding's log, in file and CLI.