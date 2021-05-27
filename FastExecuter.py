import re


class FastExecuter:
    def fast_execute(code):
        func_prototype = re.search("def.*:", code)
        if func_prototype:
            if re.search("main", func_prototype.group()):
                return code
            func_call = func_prototype.group().replace("def", "result =")
            func_call = func_call.replace(":", "")
        else:
            func_call = "# no functions found"

        main_exists = re.search("def.main\(\):", code)
        print(main_exists)
        if main_exists:
            main = code[0: main_exists.start()] + "def main():\n    " + func_call + "\n    "
        else:
            main = code +  "\n\ndef main():\n    " + func_call + "\n    "

        return main
