#!/usr/bin/env python
# coding=utf-8
"""Unit tests for pyiosxr, a module to interact with Cisco devices running IOS-XR."""

import sys
import mock
import unittest
from xml.etree import ElementTree

import pexpect
from pyIOSXR import IOSXR
from pyIOSXR.iosxr import __execute_show__, __execute_config_show__, __execute_rpc__
from pyIOSXR.exceptions import XMLCLIError, InvalidInputError, TimeoutError, EOFError, IteratorIDError


# test helpers

# def __execute_rpc__(device, rpc_command, timeout):

class TestExecuteRpc(unittest.TestCase):

    def test_execute_rpc_XMLCLIError(self):
        '''
        Test pyiosxr helper __execute_rpc__
        Should return XMLCLIError
        '''
        def sendline(foo):
            pass
        def expect_exact(foo, timeout):
            return 1
        device = mock.Mock()
        setattr(device, 'sendline', sendline)
        setattr(device, 'expect_exact', expect_exact)
        self.assertRaises(XMLCLIError, __execute_rpc__, device=device, rpc_command='<Get></Get>', timeout=10)

    def test_execute_rpc_TimeoutError(self):
        '''
        Test pyiosxr helper __execute_rpc__
        Should return TimeoutError
        '''
        def sendline(foo):
            pass
        def expect_exact(foo, timeout):
            raise pexpect.TIMEOUT('error')
        device = mock.Mock()
        setattr(device, 'sendline', sendline)
        setattr(device, 'expect_exact', expect_exact)
        self.assertRaises(TimeoutError, __execute_rpc__, device=device, rpc_command='<Get></Get>', timeout=10)

    def test_execute_rpc_EOFError(self):
        '''
        Test pyiosxr helper __execute_rpc__
        Should return EOFError
        '''
        def sendline(foo):
            pass
        def expect_exact(foo, timeout):
            raise pexpect.EOF('error')
        device = mock.Mock()
        setattr(device, 'sendline', sendline)
        setattr(device, 'expect_exact', expect_exact)
        self.assertRaises(EOFError, __execute_rpc__, device=device, rpc_command='<Get></Get>', timeout=10)

    def test_execute_rpc_device_close_xml(self):
        '''
        Test pyiosxr helper __execute_rpc__ with responses from xml files
        Should return ElementTree.Element object
        '''
        def sendline(foo):
            pass
        def expect_exact(foo, timeout):
            return 0
        device = mock.Mock()
        setattr(device, 'sendline', sendline)
        setattr(device, 'expect_exact', expect_exact)
        setattr(device, 'match', '')
        setattr(device, 'before', open('test/device_close.xml').read())
        self.assertIsInstance(__execute_rpc__(device=device, rpc_command='<Get></Get>', timeout=10), ElementTree.Element)

    def test_execute_rpc_device_commit_config_xml(self):
        '''
        Test pyiosxr helper __execute_rpc__ with responses from xml files
        Should return ElementTree.Element object
        '''
        def sendline(foo):
            pass
        def expect_exact(foo, timeout):
            return 0
        device = mock.Mock()
        setattr(device, 'sendline', sendline)
        setattr(device, 'expect_exact', expect_exact)
        setattr(device, 'match', '')
        setattr(device, 'before', open('test/device_commit_config.xml').read())
        self.assertIsInstance(__execute_rpc__(device=device, rpc_command='<Get></Get>', timeout=10), ElementTree.Element)

    def test_execute_rpc_device_compare_config_xml(self):
        '''
        Test pyiosxr helper __execute_rpc__ with responses from xml files
        Should return ElementTree.Element object
        '''
        def sendline(foo):
            pass
        def expect_exact(foo, timeout):
            return 0
        device = mock.Mock()
        setattr(device, 'sendline', sendline)
        setattr(device, 'expect_exact', expect_exact)
        setattr(device, 'match', '')
        setattr(device, 'before', open('test/device_compare_config.xml').read())
        self.assertIsInstance(__execute_rpc__(device=device, rpc_command='<Get></Get>', timeout=10), ElementTree.Element)

    def test_execute_rpc_device_discard_config_xml(self):
        '''
        Test pyiosxr helper __execute_rpc__ with responses from xml files
        Should return ElementTree.Element object
        '''
        def sendline(foo):
            pass
        def expect_exact(foo, timeout):
            return 0
        device = mock.Mock()
        setattr(device, 'sendline', sendline)
        setattr(device, 'expect_exact', expect_exact)
        setattr(device, 'match', '')
        setattr(device, 'before', open('test/device_discard_config.xml').read())
        self.assertIsInstance(__execute_rpc__(device=device, rpc_command='<Get></Get>', timeout=10), ElementTree.Element)

    def test_execute_rpc_device_load_candidate_config_xml(self):
        '''
        Test pyiosxr helper __execute_rpc__ with responses from xml files
        Should return ElementTree.Element object
        '''
        def sendline(foo):
            pass
        def expect_exact(foo, timeout):
            return 0
        device = mock.Mock()
        setattr(device, 'sendline', sendline)
        setattr(device, 'expect_exact', expect_exact)
        setattr(device, 'match', '')
        setattr(device, 'before', open('test/device_load_candidate_config.xml').read())
        self.assertIsInstance(__execute_rpc__(device=device, rpc_command='<Get></Get>', timeout=10), ElementTree.Element)

    def test_execute_rpc_device_make_rpc_call_xml(self):
        '''
        Test pyiosxr helper __execute_rpc__ with responses from xml files
        Should return ElementTree.Element object
        '''
        def sendline(foo):
            pass
        def expect_exact(foo, timeout):
            return 0
        device = mock.Mock()
        setattr(device, 'sendline', sendline)
        setattr(device, 'expect_exact', expect_exact)
        setattr(device, 'match', '')
        setattr(device, 'before', open('test/device_make_rpc_call.xml').read())
        self.assertIsInstance(__execute_rpc__(device=device, rpc_command='<Get></Get>', timeout=10), ElementTree.Element)

    def test_execute_rpc_device_open_xml(self):
        '''
        Test pyiosxr helper __execute_rpc__ with responses from xml files
        Should return ElementTree.Element object
        '''
        def sendline(foo):
            pass
        def expect_exact(foo, timeout):
            return 0
        device = mock.Mock()
        setattr(device, 'sendline', sendline)
        setattr(device, 'expect_exact', expect_exact)
        setattr(device, 'match', '')
        setattr(device, 'before', open('test/device_open.xml').read())
        self.assertIsInstance(__execute_rpc__(device=device, rpc_command='<Get></Get>', timeout=10), ElementTree.Element)

    def test_execute_rpc_device_rollback_xml(self):
        '''
        Test pyiosxr helper __execute_rpc__ with responses from xml files
        Should return ElementTree.Element object
        '''
        def sendline(foo):
            pass
        def expect_exact(foo, timeout):
            return 0
        device = mock.Mock()
        setattr(device, 'sendline', sendline)
        setattr(device, 'expect_exact', expect_exact)
        setattr(device, 'match', '')
        setattr(device, 'before', open('test/device_rollback.xml').read())
        self.assertIsInstance(__execute_rpc__(device=device, rpc_command='<Get></Get>', timeout=10), ElementTree.Element)

    def test_execute_rpc_device_close_xml(self):
        '''
        Test pyiosxr helper __execute_rpc__ with responses from xml files
        Should return ElementTree.Element object
        '''
        def sendline(foo):
            pass
        def expect_exact(foo, timeout):
            return 0
        device = mock.Mock()
        setattr(device, 'sendline', sendline)
        setattr(device, 'expect_exact', expect_exact)
        setattr(device, 'match', '')
        setattr(device, 'before', open('test/device_show_interfaces.xml').read())
        self.assertIsInstance(__execute_rpc__(device=device, rpc_command='<Get></Get>', timeout=10), ElementTree.Element)

    def test_execute_rpc_device_load_candidate_config_invalid_input_xml(self):
        '''
        Test pyiosxr helper __execute_rpc__ with responses from xml files
        Should return InvalidInputError
        '''
        def sendline(foo):
            pass
        def expect_exact(foo, timeout):
            return 0
        device = mock.Mock()
        setattr(device, 'sendline', sendline)
        setattr(device, 'expect_exact', expect_exact)
        setattr(device, 'match', '')
        setattr(device, 'before', open('test/device_load_candidate_config_invalid_input.xml').read())
        self.assertRaises(InvalidInputError, __execute_rpc__, device=device, rpc_command='<Get></Get>', timeout=10)

    def test_execute_rpc_device_iterator_id_error_xml(self):
        '''
        Test pyiosxr helper __execute_rpc__ with responses from xml files
        Should return IteratorIDError
        '''
        def sendline(foo):
            pass
        def expect_exact(foo, timeout):
            return 0
        device = mock.Mock()
        setattr(device, 'sendline', sendline)
        setattr(device, 'expect_exact', expect_exact)
        setattr(device, 'match', '')
        setattr(device, 'before', open('test/device_iterator_id_error.xml').read())
        self.assertRaises(IteratorIDError, __execute_rpc__, device=device, rpc_command='<Get></Get>', timeout=10)


# def __execute_show__(device, show_command, timeout):

class TestExecuteShow(unittest.TestCase):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_rpc__')
    def test_execute_show(self, mock_rpc, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr helper __execute_show__
        Should return True
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        self.assertTrue(__execute_show__(device=device, show_command='show interfaces', timeout=10))


# def __execute_config_show__(device, show_command, timeout):

class TestExecuteConfigShow(unittest.TestCase):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_rpc__')
    def test_execute_config_show(self, mock_rpc, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr helper __execute_config_show__
        Should return True
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        self.assertTrue(__execute_config_show__(device=device, show_command='show interfaces', timeout=10))


# test class IOSXR

#     def __init__(self, hostname, username, password, port=22, timeout=60, logfile=None, lock=True):

class TestInit(unittest.TestCase):

    def test_init(self):
        '''
        Test pyiosxr class init
        Should return True
        '''
        self.assertTrue(IOSXR(hostname='hostname', username='ejasinska', password='passwd'))

    def test_init_no_lock(self):
        '''
        Test pyiosxr class init - woithout locking
        Should return True
        '''
        self.assertTrue(IOSXR(hostname='hostname', username='ejasinska', password='passwd', lock=False))

    def test_init_log_stdout(self):
        '''
        Test pyiosxr class init - log to stdout
        Should return True
        '''
        self.assertTrue(IOSXR(hostname='hostname', username='ejasinska', password='passwd', logfile=sys.stdout))

    def test_init_log_file(self):
        '''
        Test pyiosxr class init - log to file
        Should return True
        '''
        self.assertTrue(IOSXR(hostname='hostname', username='ejasinska', password='passwd', logfile='filehandle'))

    def test_init_port(self):
        '''
        Test pyiosxr class init - pass port number
        Should return True
        '''
        self.assertTrue(IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22))

    def test_init_timeout(self):
        '''
        Test pyiosxr class init - pass timeout
        Should return True
        '''
        self.assertTrue(IOSXR(hostname='hostname', username='ejasinska', password='passwd', timeout=120))


#     def __getattr__(self, item):

class TestGetattr(unittest.TestCase):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_show__')
    def test_getattr_show(self, mock_show, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class getattr
        Should return True
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        mock_show.return_value = '!! IOS XR Configuration !@#$ </Exec>'
        self.assertTrue(device.show_interface("GigabitEthernet0/0/0/0"))

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_config_show__')
    def test_getattr_show_config(self, mock_show, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class getattr
        Should return True
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        mock_show.return_value = '!! IOS XR Configuration !@#$ </Exec>'
        self.assertTrue(device.show_configuration_merge(config=True))

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    def test_getattr_AttributeError(self, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class getattr
        Should return AttributeError
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        self.assertRaises(AttributeError, getattr, device, 'foo')


#     def open(self):

class TestOpen(unittest.TestCase):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn')
    @mock.patch('pyIOSXR.iosxr.IOSXR.lock')
    def test_open(self, mock_lock, mock_spawn):
        '''
        Test pyiosxr class open
        Should return None
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=True)
        self.assertIsNone(device.open())

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn')
    def test_open_no_lock(self, mock_spawn):
        '''
        Test pyiosxr class open - without lock
        Should return None
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        self.assertIsNone(device.open())

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    def test_open_ssh_key_yes(self, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class open - with ssh key warning
        Should return Nona
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        mock_expect.return_value = 0
        self.assertIsNone(device.open())

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    def test_open_no_passwd(self, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class open - pexpect.EOF
        Should return Nona
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        mock_expect.return_value = 3
        self.assertIsNone(device.open())

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    def test_open_TimeoutError(self, mock_expect, mock_spawn):
        '''
        Test pyiosxr class open - raising pexpect.TIMEOUT
        Should return TimeoutError
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=True)
        mock_spawn.return_value = None
        mock_expect.side_effect = pexpect.TIMEOUT('error')
        self.assertRaises(TimeoutError, device.open)

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    def test_open_EOFError(self, mock_expect, mock_spawn):
        '''
        Test pyiosxr class open - raising pexpect.EOF
        Should return EOFError
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=True)
        mock_spawn.return_value = None
        mock_expect.side_effect = pexpect.EOF('error')
        self.assertRaises(EOFError, device.open)

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    def test_open_XMLCLIError(self, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class open - error as if XML not enabled on device: ERROR: 0x24319600
        Should return XMLCLIError
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=True)
        mock_spawn.return_value = None
        # expect returns 1 to raise XMLCLIError
        mock_expect.return_value = 1
        self.assertRaises(XMLCLIError, device.open)


#     def close(self):

class TestClose(unittest.TestCase):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.close')
    def test_close(self, mock_close, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class close
        Should return None
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        self.assertIsNone(device.close())

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.close')
    @mock.patch('pyIOSXR.iosxr.IOSXR.lock')
    @mock.patch('pyIOSXR.iosxr.__execute_rpc__')
    def test_close_locked(self, mock_rpc, mock_lock, mock_close, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class close with lock
        Should return None
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=True)
        mock_spawn.return_value = None
        device.open()
        self.assertIsNone(device.close())


#     def lock(self):

class TestLock(unittest.TestCase):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_rpc__')
    def test_lock(self, mock_rpc, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class lock
        Should return None
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        self.assertIsNone(device.lock())


#     def unlock(self):

class TestUnlock(unittest.TestCase):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.IOSXR.lock')
    @mock.patch('pyIOSXR.iosxr.__execute_rpc__')
    def test_unlock(self, mock_rpc, mock_lock, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class unlock
        Should return None
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=True)
        mock_spawn.return_value = None
        device.open()
        device.locked = True
        self.assertIsNone(device.unlock())


#     def discard_config(self):

class TestDiscardConfig(unittest.TestCase):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_rpc__')
    def test_discard_config(self, mock_rpc, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class discard_config
        Should return None
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        self.assertIsNone(device.discard_config())


#     def rollback(self):

class TestRollback(unittest.TestCase):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_rpc__')
    def test_rollback(self, mock_rpc, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class rollback
        Should return None
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        self.assertIsNone(device.rollback())


#     def make_rpc_call(self, rpc_command):

class TestMakeRpcCall(unittest.TestCase):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_rpc__')
    def test_make_rpc_call(self, mock_rpc, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class make_rpc_call
        Should return True
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        mock_rpc.return_value = ElementTree.fromstring('<xml></xml>')
        device.open()
        self.assertTrue(device.make_rpc_call("<Get><Operational><LLDP><NodeTable></NodeTable></LLDP></Operational></Get>"))


#     def load_candidate_config(self, filename=None, config=None):

class TestLoadCandidateConfig(unittest.TestCase):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_rpc__')
    def test_load_candidate_config_file(self, mock_rpc, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class load_candidate_config
        Should return None
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        self.assertIsNone(device.load_candidate_config(filename='test/config.txt'))

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_rpc__')
    def test_load_candidate_config(self, mock_rpc, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class load_candidate_config
        Should return None
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        self.assertIsNone(device.load_candidate_config(config='config'))

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.IOSXR.discard_config')
    @mock.patch('pyIOSXR.iosxr.__execute_rpc__')
    def test_load_candidate_config_InvalidInputError(self, mock_rpc, mock_discard, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class load_candidate_config
        Should return InvalidInputError
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        mock_rpc.side_effect = InvalidInputError('error')
        device.open()
        self.assertRaises(InvalidInputError, device.load_candidate_config, config='config')


#     def get_candidate_config(self, merge=False, formal=False):

class TestGetCandidateConfig(unittest.TestCase):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_config_show__')
    def test_get_candidate_config(self, mock_show, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class get_candidate_config
        Should return True
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        mock_show.return_value = '!! IOS XR Configuration'
        self.assertTrue(device.get_candidate_config(merge=True, formal=True))


#     def compare_config(self):

class TestCompareConfig(unittest.TestCase):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_config_show__')
    def test_compare_config(self, mock_show, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class compare_config
        Should return True
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        mock_show.return_value = ''
        self.assertEqual('', device.compare_config())


#     def compare_replace_config(self):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_config_show__')
    def test_compare_replace_config(self, mock_show, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class compare_replace_config
        Should return True
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        mock_show.return_value = ''
        self.assertEqual('', device.compare_replace_config())


#     def commit_config(self, label=None, comment=None, confirmed=None):

class TestCommitConfig(unittest.TestCase):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_rpc__')
    def test_commit_config(self, mock_rpc, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class commit_config
        Should return None
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        self.assertIsNone(device.commit_config(label='label', comment='comment', confirmed=30))

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_rpc__')
    def test_commit_config_InvalidInputError(self, mock_rpc, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class commit_config
        Should return InvalidInputError
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        self.assertRaises(InvalidInputError, device.commit_config, label='label', comment='comment', confirmed=900)


#     def commit_replace_config(self, label=None, comment=None, confirmed=None):

class TestCommitReplaceConfig(unittest.TestCase):

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_rpc__')
    def test_commit_replace_config(self, mock_rpc, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class commit_replace_config
        Should return None
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        self.assertIsNone(device.commit_replace_config(label='label', comment='comment', confirmed=30))

    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.__init__')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.expect')
    @mock.patch('pyIOSXR.iosxr.pexpect.spawn.sendline')
    @mock.patch('pyIOSXR.iosxr.__execute_rpc__')
    def test_commit_replace_config_InvalidInputError(self, mock_rpc, mock_sendline, mock_expect, mock_spawn):
        '''
        Test pyiosxr class commit_replace_config
        Should return InvalidInputError
        '''
        device = IOSXR(hostname='hostname', username='ejasinska', password='passwd', port=22, timeout=60, logfile=None, lock=False)
        mock_spawn.return_value = None
        device.open()
        self.assertRaises(InvalidInputError, device.commit_replace_config, label='label', comment='comment', confirmed=900)


if __name__ == '__main__':
    unittest.main()
