WinWait("[CLASS:#32770]","",10)
ControlFocus("��","","Edit1")
;ʶ��windows����
WinWait("[CLASS:#32770]","",10)
;���ڵȴ�ʮ��
ControlSetText("��", "", "Edit1", "D:\WebSelenium\PushFile\test.xls")
;���������������Ҫ�ϴ��ĵ�ַ
 Sleep(2000)
ControlClick("��", "","Button1");
;���[�򿪡���ť