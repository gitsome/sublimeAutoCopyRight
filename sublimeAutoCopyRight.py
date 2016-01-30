'''
Original license string generation from:
http://stackoverflow.com/questions/15709753/sublime-text-2-plugin-to-enter-auto-license-comment-line-with-specific-format
'''

import sublime, sublime_plugin
import os
import datetime
import random
import getpass
import re
import json

def AddCopyRightStamp(self, view):

    company_name = view.settings().get("copyRightInfo").get("name")
    company_site = view.settings().get("copyRightInfo").get("site")
    company_license = view.settings().get("copyRightInfo").get("licenseText")

    edit = view.begin_edit()

    file_path = view.file_name()
    file_name = os.path.basename(file_path)
    year = datetime.datetime.utcnow().strftime("%Y")
    date_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    random_number = str(random.randrange(0000, 9999)).zfill(4)
    user = getpass.getuser()

    '''
    /**
    * @version   $Id: ${1:current_file_name.extension} ${2:random_4_digit_number} ${3:YYYY-MM-DD} ${4:time_in_UTC_24} ${5:current_logged-in_user} $
    * @author    Company http://example.com
    * @copyright Copyright (C) 2007 - ${6:current_year} Company
    * @license   http://www.gnu.org/licenses/gpl-2.0.html GNU/GPLv2 only
    */
    '''

    copyRight = "/** COPYRIGHT\n"
    copyRight += "* @version   $Id: " + file_name + " " + random_number + " " + date_time + " " + user + " $\n"
    copyRight += "* @author    " + company_name + " " + company_site + "\n"
    copyRight += "* @copyright Copyright (C) 2007 - " + year + " " + company_name + "\n"
    copyRight += "* @license   " + company_license + "\n"
    copyRight += "*/\n\n"

    topPoint = view.text_point(0,0)

    view.insert(edit, topPoint, copyRight)
    view.end_edit(edit)


def hasCopyRightStamp(self, view):
    copyRightMatches = view.find_all('\/\*\* COPYRIGHT')
    return len(copyRightMatches) != 0


class AddCopyRightStampListener(sublime_plugin.EventListener):

    def on_pre_save(self, view):

        if view.settings().get("copyRightInfo") == None:
            return

        if hasCopyRightStamp(self, view) == False:
            AddCopyRightStamp(self, view)