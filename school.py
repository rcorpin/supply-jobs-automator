import mechanize
import threading

UserId = '211752'
Password = '73778458'
Url = 'https://tdsb.eschoolsolutions.com/substituteAvailableJobInitAction.do'
SearchResultUrl = 'https://tdsb.eschoolsolutions.com/substituteAvailableJobAction.do'
SearchToDate = '06/30/2016'

browser = mechanize.Browser()

browser.open(Url)

browser.select_form( name="logOnForm" )
browser.form['userID'] = UserId
browser.form['userPin'] = Password
browser.submit()

url = browser.open(Url)

def searchJobs ():
  browser.select_form( name="reviewAssignForm" )
  
  endDateInput = browser.form.find_control("endDate")
  endDateInput.disabled = False
  endDateInput.value = SearchToDate
 
  for control in browser.form.controls:
    print control

  response = browser.submit()

  #url = browser.open(SearchResultUrl)

  f = open('response.html','w')
  f.write(response.read())
  f.close()

  print "Search Complete!"

  threading.Timer(16, searchJobs).start()

searchJobs()
