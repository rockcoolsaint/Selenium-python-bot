from booking.booking import Booking

try:
  with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='GBP')
    bot.select_place_to_go(input("Where do you want to go? "))
    bot.select_dates(check_in_date=input("What is the check_in_date? format:'YYYY-MM-DD' "),
                     check_out_date=input("What is the check_out_date? format:'YYYY-MM-DD' "))
    bot.select_adults(int(input("How many people? ")))
    bot.click_search()
    bot.apply_filterations()
    bot.refresh() # A workaround to let out bot grab the data properly
    bot.report_results()

except Exception as e:
  if 'in PATH' in str(e):
    print(
      'You are trying to run the bot from command line \n'
      'Please add to PATH your Selenium Drivers \n'
      'Windows: \n'
      '    set PATH=%PATH%;C:path-to-your-folder \n \n'
      'Linux: \n'
      '    PATH=$PATH:/path/to/your/folder/ \n'
    )
  else:
    raise