
class SignInFormValidator:

    @staticmethod
    def is_valid(**kwargs) -> bool:
        if (len(kwargs['username']) != 0 and len(kwargs['password']) != 0):
            return True
        else:
            return False


