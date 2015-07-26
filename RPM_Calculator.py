def function():
    ms = float(raw_input())
    
    ms /= 1000
        
    ms = 60 / ms
    
    print "%s rounds per minute" % ms
    function()
function()

#100 is 600 rpm

#75 is 800 rpm