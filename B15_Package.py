# import module cần có file __init__ 
import package.myPackage as tenModule
print(tenModule.max(7, 11))
print(tenModule.min(7, 11))


#  module con của module 

import package.moduleCon.say as conCon
conCon.sayHello("Song")
conCon.sayGoodbye("Song")