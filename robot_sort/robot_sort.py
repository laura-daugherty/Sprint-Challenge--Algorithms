class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

 




    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        self.set_light_off()
        while self.can_move_right():
            self.swap_item()
            self.move_right()
            if self.compare_item() == 1:
                self.swap_item()
                self.set_light_on()
            self.move_left()
            self.swap_item()
            self.move_right()
        while self.can_move_left():
            self.move_left()
        if self.light_is_on():
            self.sort()
        else:
            return
#set light off
#while can move right:
    #pick up first item (swap)
    #move_right()
    #COMPARING
    #if compare == 1
        #swap
        #turn on light
    #move left
    #swap
    #move right

#while can move left:
    #move_left
#if self.light_is_on:
#   self.sort()
#else:
    #return




    # def bubble_sort( arr ):
    # for i in range(0, len(arr)):
    #     swapped = True
    #     while swapped is True:
    #         for j in range(i, len(arr)):
    #             if arr[j] < arr[i]:
    #                 temp = arr[i]
    #                 arr[i] = arr[j]
    #                 arr[j] = temp
    #                 swapped = True
    #             else:
    #                 swapped = False
    # return arr


        # if we get to the end of the list and the light is on, the array is sorted
        

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)

# custom robot methods
    # def find_length(self):
    #     count = 0
    #     while self.can_move_right() == True:
    #         self.move_right()
    #         count += 1
    #     return count

    # def move_to(self, i):
    #     while self.can_move_left():
    #         self.move_left()
    #     for j in range(0, i):
    #         self.move_right()

    # def swap(self, i, j):
    #     # pick up arr[i]
    #     self.move_to(i)
    #     self.swap_item()

    #     # swap with arr[j]
    #     self.move_to(j)
    #     self.swap_item()

    #     # place arr[j] in arr[i]
    #     self.move_to(i)
    #     self.swap_item()
        
    # def compare(self, i, j):
    #     self.move_to(i)
    #     self.swap_item()

    #     self.move_to(j)
    #     comparison = self.compare_item()
    #     self.move_to(i)
    #     self.swap_item()

    #     return comparison

    # def sort(self):
    #     """
    #     Sort the robot's list.
    #     """
    #     # Fill this out

    #     print(self._position)
    #     print(self._item)
    #     print(self._list)

    #     for i in range(0, self.find_length()):
    #         print("outer", self._list)
    #         print("i", i)
    #         for j in range(0, self.find_length() - i - 1):
    #             print("  inner", self._list)
    #             print("  j", j)
    #             if self.compare(j, j + 1):
    #                 print("  swapping")
    #                 self.swap(j, j + 1)
    #                 print("  swapped", self._list)

    #         print("done with inner loop", self._list)
                        
    #     return self._list


    # while self.can_move_right():
    #         print("at beginning")
    #         print(self._list)
    #         # swap
    #         if self._item == None:
    #             print("have none, picking up item")
    #             self.swap_item()
    #         else:
    #             # if the held item is less than the item at this point in the list, swap
    #             if self.compare_item() == 1:
    #                 print("held item is less or none")
    #                 self.swap_item()
    #                 self.set_light_off()
    #             elif self.compare_item == 0 or self.compare_item == -1:

    #         # traversal    
    #         if self.can_move_right():
    #             print("moving right-ooo")
    #             self.move_right()
    #         else:
    #             print("resetting back to beginning")
    #             # drop what we have, go back to beginning, turn light back on
    #             self.set_light_on()
    #             self.swap_item()
    #             while self.can_move_left():
    #                 self.move_left()
        
