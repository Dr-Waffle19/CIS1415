def shampoo_instructions(num_cycles):
   if num_cycles < 1:
      print("Too few")
   elif num_cycles > 4:
      print ("Too many.")
   else:
        i = 0
        while i<num_cycles:
            print (i+1,": Lather and rinse.")
            i = i + 1
   print('Done.')

shampoo_instructions(2)
