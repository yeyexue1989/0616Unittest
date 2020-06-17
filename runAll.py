import unittest
import HtmlTestRunner
from InsuranceManage.EmergencyManageNew import EmergencyManageNew
from InsuranceManage.EmergencyManageEdit import EmergencyManageExmine

if __name__ == '__main__':

    suite = unittest.TestSuite()
    #应急预案新建
    suite.addTest(EmergencyManageNew("test_emergency_manage_new"))
    #应急预案编辑
    suite.addTest(EmergencyManageExmine("test_emergency_manage_exmine"))
    with open('report.html','w') as f:
        runner = HtmlTestRunner.HTMLTestRunner(stream = f,verbosity=2)
        runner.run(suite)