import unittest,time
# from HtmlTestRunner import HTMLTestRunner
import HtmlTestRunner
from prepare_and_accept.prepare_new import prepareNewClass
from prepare_and_accept.prepare_report import  prepareReportClass
from prepare_and_accept.prepare_examine_team_monitor import prepareExamine
from prepare_and_accept.prepare_examine_zhuanzhe import prepareExamineZhuanzhe
from prepare_and_accept.prepare_report2 import prepareReport2
from prepare_and_accept.prepare_examine2_monitor import prepareExamine2Monitor
from prepare_and_accept.prepare_examine2_zhuanzhe import prepareExamine2Zhuanzhe
from prepare_and_accept.prepare_report3 import prepareReport3
from prepare_and_accept.prepare_examine3_monitor import PrepareExamine3Monitor
from prepare_and_accept.prepare_examine3_zhuanzhe import prepareExamine3Zhuanzhe
from prepare_and_accept.prepare_report4 import prepareReport4
from prepare_and_accept.prepare_examine4_monitor import prepareExamine4Monitor
from prepare_and_accept.prepare_examine4_zhuanzhe import prepareExamine4Zhuanzhe
from prepare_and_accept.prepare_examine4_leader import prepareExamine4Leader
from prepare_and_accept.prepare_report5 import prepareReport5
# from FJAD.prepare_and_accept.prepare_examine5_monitor import prepareExamine5Monitor
# from FJAD.prepare_and_accept.prepare_examine5_zhuanze import prepareExamine5Zhuanze
# from FJAD.prepare_and_accept.prepare_examine5_leader import prepareExamine5Leader
if __name__ == '__main__':
    suite = unittest.TestSuite()
    #工程可研
    suite.addTest(prepareNewClass('test_prepare_new'))  #班员新建工程
    suite.addTest(prepareReportClass('test_prepare_report'))   #班员上报
    suite.addTest(prepareExamine('test_prepare_examine'))    #班长审核
    suite.addTest(prepareExamineZhuanzhe('test_prepare_examine_zhuanzhe'))  #专责审核
    #工程初设
    suite.addTest(prepareReport2('test_prepare_report2'))   #班员上报
    suite.addTest(prepareExamine2Monitor('test_prepare_examine2_monitor')) #班长审核
    suite.addTest(prepareExamine2Zhuanzhe('test_prepare_examine2_zhuanzhe')) #专责审核
    #工程施工
    suite.addTest(prepareReport3('test_prepare_report3'))   #班员上报
    suite.addTest(PrepareExamine3Monitor('test_prepare_examine3_monitor'))   #班长审核
    suite.addTest(prepareExamine3Zhuanzhe('test_prepare_examine3_zhuanzhe'))  #专责审核
    #工程试验
    suite.addTest(prepareReport4('test_prepare_report4'))   #班员上报
    suite.addTest(prepareExamine4Monitor('test_prepare_examine4_monitor'))   #班长审核
    suite.addTest(prepareExamine4Zhuanzhe('test_prepare_examine4_zhuanzhe'))   #专责审核
    suite.addTest(prepareExamine4Leader('test_prepare_examine4_leader'))   #领导审核
    # #工程验收
    suite.addTest(prepareReport5('test_prepare_report5'))   #班员上报
    # suite.addTest(prepareExamine5Monitor('test_prepare_examine5_monitor'))   #班长审核
    # suite.addTest(prepareExamine5Zhuanze('test_prepare_examine5_zhuanze'))   #专责审核
    # suite.addTest(prepareExamine5Leader('test_prepare_examine5_leader'))     #领导审核
    with open("res.html","w") as f:
        # runner = unittest.TextTestRunner(stream=f,descriptions="测试报告",verbosity=2)
        runner = HtmlTestRunner.HTMLTestRunner(stream=f,descriptions='测试情况',verbosity=2)
        runner.run(suite)

