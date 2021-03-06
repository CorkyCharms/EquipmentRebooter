####################################################################
###                        ***TO DO LIST***                      ###
### Send an email once reboot has been initiated                 ###
### Send confirmation email 10 Mins prior to command, confirming ###              
### Loop back and ask if user would like to add another job      ###
### Count down time until command is initiated                   ###
### Working on getting the user to pick the day of the week      ###
####################################################################

import paramiko
import schedule
import time

equipment_ip = input("Please eneter the IP of the equipment: ")
equipment_username = input("Please eneter the Username of the equipment: ")
equipment_password = input("Please eneter the Password of the equipment: ")
equipment_command_schedule_day = input("Please enter the day you would like to schedule the command: ")
equipment_command_schedule_time = input("Please enter the time you would like to schedule the command: ")

SSH = paramiko.SSHClient()

#Loading SSH host keys
SSH.load_system_host_keys()
SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())

SSH.connect(
    equipment_Ip,
    username = equipment_username,
    password = equipment_password,
    look_for_keys = False
)

#Commands that will run(reboot)
def reboot_equipment_command():
    SSH.exec_command("/sbin/reboot -f > /dev/null 2>&1 &")
    return schedule.CancelJob


#time that command will run.
schedule.every().monday.at(equipment_command_schedule_time).do(reboot_equipment_command)

all_jobs = schedule.get_jobs()
print(all_jobs)

while True:
    schedule.run_pending()
    time.sleep(1)




