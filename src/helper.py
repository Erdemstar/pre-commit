import os,sys
class Helper:
    
    @staticmethod
    def last_char_control(str,char):
        """
        Description : This is used for control last str of string is char which is giving or not. If str has not char, it append.
        """
        if str is not None:
            if str[-1] != char:
                return str + char
            else:
                return str

    @staticmethod
    def get_current_path():
        """
        Description : This is used to return current directory path.ß 
        """
        return os.getcwd()
    
    @staticmethod
    def close_type(number:int):
        """
        Description : This function is used to force close app is normal or error.ß
        """
        sys.exit(number)
    