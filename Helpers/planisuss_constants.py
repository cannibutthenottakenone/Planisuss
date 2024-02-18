from json import loads

def import_constants(**kargs) -> dict:
    """
    ### import_constants() 
    Initializes the program constants, it uses the parameters provided and defaults to the constants json file.
    
    parameters are a **kargs, see docs for constants names.
    """
    constants=loads(open("constants.json").read())
    keys=kargs.keys()
    
    for e in constants["WORLD"].keys():
        if e in keys:
            constants["WORLD"][e]=kargs[e]
            
    for e in constants["CREATURES"].keys():
        if e in keys:
            constants["CREATURES"][e]=kargs[e]
            
    for e in constants["CREATURES"]["ERBAST"].keys():
        if e in keys:
            constants["CREATURES"]["ERBAST"][e]=kargs[e]
            
    for e in constants["CREATURES"]["CARVIZ"].keys():
        if e in keys:
            constants["CREATURES"]["CARVIZ"][e]=kargs[e]
            
    return constants
    
