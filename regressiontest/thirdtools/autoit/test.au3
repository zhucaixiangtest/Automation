WinWait("[CLASS:#32770]","",10)
ControlFocus("��","","Edit1")
;ʶ��windows����
WinWait("[CLASS:#32770]","",5)
;���ڵȴ�ʮ��
ControlSetText("��", "", "Edit1", "F:\testWeb\UI\regressiontest\download")
;���������������Ҫ�ϴ��ĵ�ַ
 Sleep(2000)
ControlClick("��", "","Button1");
;���[�򿪡���ť