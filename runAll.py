import unittest
import HtmlTestRunner
from InsuranceManage.EmergencyManageNew import EmergencyManageNew
from InsuranceManage.EmergencyManageEdit import EmergencyManageEdit
from InsuranceManage.EmergencyManageExamine import EmergencyManageExamine
from InsuranceManage.SparePartsNew import SparePartsNew
if __name__ == '__main__':

    suite = unittest.TestSuite()
    #应急预案新建
    suite.addTest(EmergencyManageNew("test_emergency_manage_new"))
    print("应急预案新建OK")
    #应急预案编辑
    suite.addTest(EmergencyManageEdit("test_emergency_manage_edit"))
    #应急预案审核
    suite.addTest(EmergencyManageExamine("test_emergency_manage_examine"))
    #备品备件新增
    suite.addTest(SparePartsNew("test_spare_parts_new"))
    with open('report.html','w') as f:
        runner = HtmlTestRunner.HTMLTestRunner(stream = f,verbosity=2)
        runner.run(suite)