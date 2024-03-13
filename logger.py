class tc: #console colors
    Header = '\033[95m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    Green = '\033[92m'
    Warn = '\033[93m'
    Fail = '\033[91m'
    End = '\033[0m'
    Bold = '\033[1m'
    Underline = '\033[4m'

def FAIL(content):
    """Sends a RED failure message in the output"""
    print(tc.Fail, content, tc.End)

def WARN(content):
    """Sends a WARN message in the output. Soft error."""
    print(tc.Warn, content, tc.End)