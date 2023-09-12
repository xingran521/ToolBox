#include<windows.h>
#include<winternl.h>

BOOL DisguiseProcess(wchar_t *lpwszPath, wchar_t *lpwszCmd);

int main()
{
	wchar_t *lpwszPath = L"c:\\windows\\system32\\calc.exe";
	wchar_t *lpwszCmd = L"yeanhoo's calc";
	DisguiseProcess(lpwszPath, lpwszCmd);
	system("pause");
}

BOOL DisguiseProcess(wchar_t *lpwszPath, wchar_t *lpwszCmd)
{
	// 打开进程获取句柄
	HANDLE hProcess = GetModuleHandle(NULL);

	PPEB peb = { 0 };
	USHORT usCmdLen = 0;
	USHORT usPathLen = 0;
	
	__asm
	{
		mov	eax,fs:[30h]
		mov peb,eax
	}
	// 获取指定进程环境块结构中的ProcessParameters, 指针指向的是指定进程空间中


	usCmdLen = 2 + 2 * wcslen(lpwszCmd);
	(*peb).ProcessParameters->CommandLine.Buffer = lpwszCmd;
	(*peb).ProcessParameters->CommandLine.Length = usCmdLen;
	// 修改指定进程环境块PEB中命令行信息, 注意指针指向的是指定进程空间中


	usPathLen = 2 + 2 * wcslen(lpwszPath);
	(*peb).ProcessParameters->ImagePathName.Buffer = lpwszPath;
	(*peb).ProcessParameters->ImagePathName.Length = usPathLen;
	// 修改指定进程环境块PEB中路径信息, 注意指针指向的是指定进程空间中

	return TRUE;
}