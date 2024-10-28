import math

class HashSet:

    #Table initialization filling it with none
    #Customize table size with hash_set (set name) = HashSet(size=x) wherein x is the desired size
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    #Computes the index using the built in function hash and gives it a more "complicated" number with the log function from math
    #We also turn the logged value back to integer to avoid float errors
    #We obtained the total ascii value of the string and the total number of characters in the string to add to the complexity in the final operation.
    #Using mod size ensures that the index is within the table size
    
    def _hash(self, key):
        hash_value = hash(key)
        log_hash = math.log(abs(hash_value))
        
        #sum of ascii values in key string
        hash_int_sum = sum(ord(char) for char in key)
        
        #number of characters in key string
        hash_char_num = len(key)
        
        log_hash_int = int(log_hash)
        
        #3 is a defined value as part of the hash function
        return (hash_int_sum * 3 * hash_char_num * log_hash_int) % self.size
    
    #Adds a key to the hash set
    #If the index is empty it makes a new set and adds the key to the new set
    #If there is an existing key then it simply adds it to the existing set
    def add(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = {key}
        else:
            self.table[index].add(key)
    
    #Checks if key is present in the hash set
    def contains(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            return key in self.table[index]
        return False
    
    #Removes key from hash set
    def remove(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            if key in self.table[index]:
                self.table[index].remove(key)
                return True
        return False
    
    def display(self):
        print("Hash Table and Stored Product Keys:")
        for index, bucket in enumerate(self.table):
            print(f"Bucket {index}: {bucket}")
    
def main():
    hash_set = HashSet(size = 20)
    
    while True:
        print("Functions: add, contains, remove, display")
        action = input("Enter your action: ").strip().lower()

        if action == "add":
            key = input("Enter the key to add: ")
            
            if key.isalnum() and len(key) == 25:
                hash_set.add(key)
                print("Added new value to the hash set.")
                
            else:
                print("Invalid product key. Product keys are alphanumeric and contain exactly 25 characters.")

        elif action == "contains":
            key = input("Enter the key to check: ")
            exists = hash_set.contains(key)
            print("Value in hash set: ", exists)

        elif action == "remove":
            key = input("Enter the key to remove: ")
            removed = hash_set.remove(key)
            if removed:
                print("Value removed")
            else:
                print("Value does not exists")
                
        elif action == "display":
            hash_set.display()
            
        elif action == "finish":
            print("Program Closed.")
            
        else:
            print("Invalid action. Please try again.")
            
main()