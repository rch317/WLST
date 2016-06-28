##Connect to the admin server
connect('weblogic','yourpassword','t3://ermsitsoa02:7002')

##Set the target server to deploy to
target = 'AdminServer'

## Read through our file and deploy what we have
with open('deploy.txt') as myFile:
    for line in myFile:
       line=line[:-1];
       ### Should probably wrap some sanity checks around this...
       appName='/orasoa/ERM_Releases/current/'+line+'.ear';

       ### Start deploying
       print '*****************'+line;
       edit()
       startEdit()
       stopApplication(appName=line1)
       undeploy(appName=line1)
       deploy(appName=line1, path=appName, targets=target)
       startApplication(appName=line1)
       save()
       activate()

### exit cleanly
exit(0);
