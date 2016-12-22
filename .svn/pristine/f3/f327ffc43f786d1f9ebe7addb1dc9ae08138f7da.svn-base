__author__ = 'bkoenighofer'

import unittest
import subprocess
import time
import os

################################################ TESTS #################################################################


class map32_comm_roz_adversary(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map32_comm" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_32_states/map.dfa",
                             "inputfiles/uav/map_32_states/communication.dfa",
                             "inputfiles/uav/map_32_states/roz.dfa",
                             "inputfiles/uav/map_32_states/adversary.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)

class map32_comm_roz(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map32_comm" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_32_states/map.dfa",
                             "inputfiles/uav/map_32_states/communication.dfa",
                             "inputfiles/uav/map_32_states/roz.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)

class map32_comm(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map32_comm" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_32_states/map.dfa",
                             "inputfiles/uav/map_32_states/communication.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)

class map32(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map32" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_32_states/map.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)


class map16_home(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map16_ugs2_comm_roz" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_16_states/home.dfa",
                             "inputfiles/uav/map_16_states/map.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)

class map16_ugs2_comm(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map16_ugs2_comm" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_16_states/ugs2.dfa",
                             "inputfiles/uav/map_16_states/map.dfa",
                             "inputfiles/uav/map_16_states/communication.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)


class map16_ugs2(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map16_ugs2" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_16_states/ugs2.dfa",
                             "inputfiles/uav/map_16_states/map.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)


class map16_ugs1_comm_roz(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map16_ugs1_comm_roz" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_16_states/ugs1.dfa",
                             "inputfiles/uav/map_16_states/map.dfa",
                             "inputfiles/uav/map_16_states/communication.dfa",
                             "inputfiles/uav/map_16_states/roz.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)

class map16_ugs1_comm(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map16_ugs1_comm" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_16_states/ugs1.dfa",
                             "inputfiles/uav/map_16_states/map.dfa",
                             "inputfiles/uav/map_16_states/communication.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)

class map16_ugs1(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map16_ugs1" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_16_states/map.dfa",
                             "inputfiles/uav/map_16_states/ugs1.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)



class map16_comm_roz_adversary(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map16_com_roz_adversary" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_16_states/map.dfa",
                             "inputfiles/uav/map_16_states/communication.dfa",
                             "inputfiles/uav/map_16_states/roz.dfa",
                             "inputfiles/uav/map_16_states/adversary.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)



class map16_comm_roz(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map16_com_roz" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_16_states/map.dfa",
                             "inputfiles/uav/map_16_states/communication.dfa",
                             "inputfiles/uav/map_16_states/roz.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)


class map16_comm(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map16_com" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_16_states/map.dfa",
                             "inputfiles/uav/map_16_states/communication.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)

class map16(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map16" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_16_states/map.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)


class map8_ugs2_adversary(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map8_ugs2_adversary" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_8_states/ugs2.dfa",
                             "inputfiles/uav/map_8_states/map.dfa",
                             "inputfiles/uav/map_8_states/adversary.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)


class map8_ugs1_adversary(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map8_ugs1_adversary" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_8_states/ugs1.dfa",
                             "inputfiles/uav/map_8_states/map.dfa",
                             "inputfiles/uav/map_8_states/adversary.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)


class map8_ugs2(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map8_ugs2" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_8_states/map.dfa",
                             "inputfiles/uav/map_8_states/ugs2.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)



class map8_ugs1(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map8_ugs1" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_8_states/map.dfa",
                             "inputfiles/uav/map_8_states/ugs1.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)

class map8_adversary(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map8_adversary" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_8_states/map.dfa",
                             "inputfiles/uav/map_8_states/adversary.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)


class map8(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="fmcad_map8" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/uav/map_8_states/map.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)


class test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.exname="ex1" #has to be unique for correct timing-data!
        self.inputfilenames=["inputfiles/ex1.dfa"]
    def test_result(self):
        runShield(self.inputfilenames,self.exname,self)
    def test_timing(self):
        timeShield(self.inputfilenames,self.exname,self)


########################################## UTILITY FUNCTIONS ###########################################################

if __name__ == '__main__':
    unittest.main()

def runShield(inputfiles, exname, test=None):
    args = ["python","shield.py"]
    for file in inputfiles:
        args.append(file)
    result = subprocess.Popen(args)
    result.communicate()[0]
    returncode = result.returncode

    return returncode


def timeShield(inputfiles, exname, test):
    fname="timingdata/"+exname+".txt"

    if os.path.isfile(fname):
        f = open(fname, "r")
        prevtime = f.readline()
        datestr = f.readline()
        f.close()
        prevtime=float(prevtime)
    else:
        prevtime=99999999

    t = time.time()
    ret = runShield(inputfiles,exname, test)
    elapsed_time = round(time.time() - t,2)

    if elapsed_time<prevtime:
        if ret==100:
            f = open(fname, "w+")
            f.write(str(elapsed_time)+"\n")
            datestr = time.strftime("%d/%m/%Y %H:%M:%S")+"\n"
            f.write(datestr)
            f.close()

    print (exname+": "+str(elapsed_time) +"s     best time: "+str(prevtime)+"s @"+datestr+"")
    if prevtime==99999999:
        test.assertEqual(True,False,"first time execution. no timing to compare to.")
    else:
        test.assertAlmostEqual(prevtime,elapsed_time,None,"(prev time != cur time): timing seems off. prev time was from: "+datestr, 3.00)

    return [elapsed_time,prevtime,datestr]