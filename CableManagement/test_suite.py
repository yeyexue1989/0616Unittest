import unittest
from HtmlTestRunner import HTMLTestRunner
from CableManagement.test_Line_new import LineNewAdd
from CableManagement.test_cable_new import CableNewAdd
from CableManagement.test_cable_section_new import CableSection
from CableManagement.test_IntermediateJoint_new import IntermediateJointNew
from ddt import ddt,data
if __name__ == '__main__':
    test_path = "./"
    # discover = unittest.defaultTestLoader.discover(test_path,pattern="test*.py")
    suite = unittest.TestSuite()
    suite.addTest(LineNewAdd("test_line_new_add"))
    suite.addTest(CableNewAdd("test_cable_new_add"))
    suite.addTest(CableSection("test_cable_section"))
    # suite.addTest(CalbeSection("test_calbe_section_2_电缆段2"))
    # suite.addTest(CalbeSection("test_calbe_section_3_电缆段3"))
    # suite.addTest(CalbeSection("test_calbe_section_4_电缆段4"))
    # suite.addTest(CalbeSection("test_calbe_section_5_电缆段5"))
    # suite.addTest(CalbeSection("test_calbe_section_6_电缆段6"))
    # suite.addTest(CalbeSection("test_calbe_section_7_电缆段7"))
    # suite.addTest(IntermediateJointNew("test_intermediate_joint_new"))
    #
    with open("report.html","w") as fb:
        runner = HTMLTestRunner(stream=fb,report_title="One Line and three Cable",descriptions="create one line and three cables")
        runner.run(suite)