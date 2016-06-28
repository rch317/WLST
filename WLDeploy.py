##Connect to the admin server
connect('weblogic','yourpassword','t3://ermsitsoa02:7002')
##Set the target server to deploy to
target = 'AdminServer'
##Get the number of files that need to be deployed
count = len(open('/home/soamgr/scripts/deploy.txt','r').readlines(  ))
##Set the location of the file that has the .ear files to be deployed
f = open(r'/home/soamgr/scripts/deploy.txt','r')
##Start by opening the file and start readin line by line
print f
for i in range(count):
       line=f.readline()
       line1=line[:-1]
       appName='/orasoa/ERM_Releases/current/'+line1+'.ear'
       print '*****************'+line
       edit()
       startEdit()
       stopApplication(appName=line1)
       undeploy(appName=line1)
       deploy(appName=line1, path=appName, targets=target)
       startApplication(appName=line1)
       save()
       activate()
f.close()

