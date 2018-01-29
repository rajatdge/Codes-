import requests
import json

TV_program_data = []

data = requests.get('http://mobilelistings.tvguide.com/Listingsweb/ws/rest/schedules/80001.null/start/1517211000/duration/1440?ChannelFields=Name%2CFullName%2CNumber%2CSourceId&ScheduleFields=ProgramId%2CEndTime%2CStartTime%2CTitle%2CAiringAttrib%2CCatId&formattype=json&disableChannels=music%2Cppv%2C24hr')


tv_data = json.loads(data.text)
for i in tv_data:
 print (i)