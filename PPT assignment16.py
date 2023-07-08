#!/usr/bin/env python
# coding: utf-8

# In[2]:


#ANS:
def find_nearest_greater_frequency(arr):
    frequency = {}
    stack = []
    output = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] in frequency:
            frequency[arr[i]] += 1
        else:
            frequency[arr[i]] = 1

        if not stack or frequency[arr[i]] < frequency[arr[stack[-1]]]:
            stack.append(i)
        else:
            while stack and frequency[arr[i]] >= frequency[arr[stack[-1]]]:
                stack.pop()
            if stack:
                output[i] = arr[stack[-1]]
            stack.append(i)

    return output


# In[3]:


arr = [1, 1, 2, 3, 4, 2, 1]
output = find_nearest_greater_frequency(arr)
print(output)


# In[4]:


arr =[1, 1, 1, 2, 2, 2, 2, 11, 3, 3]
output = find_nearest_greater_frequency(arr)
print(output)


# In[5]:


#Answer2:

def sort_stack(stack):
    temp_stack = []

    while stack:
        if not temp_stack or stack[-1] >= temp_stack[-1]:
            temp_stack.append(stack.pop())
        else:
            temp = stack.pop()
            while temp_stack and temp < temp_stack[-1]:
                stack.append(temp_stack.pop())
            temp_stack.append(temp)

    return temp_stack


# Example usage:
stack = [34, 3, 31, 98, 92, 23]
sorted_stack = sort_stack(stack)
print(sorted_stack)  

stack = [3, 5, 1, 4, 2, 8]
sorted_stack = sort_stack(stack)
print(sorted_stack) 


# In[6]:


#answer3.

def delete_middle_element(stack):
    count = len(stack)
    mid_position = count // 2

    temp_stack = []

    # Push elements from original stack to temp stack until middle element
    for _ in range(mid_position):
        temp_stack.append(stack.pop())

    # Discard the middle element
    stack.pop()

    # Push back elements from temp stack to original stack
    while temp_stack:
        stack.append(temp_stack.pop())

    return stack


# Example usage:
stack = [1, 2, 3, 4, 5]
modified_stack = delete_middle_element(stack)
print(modified_stack)

stack = [1, 2, 3, 4, 5, 6]
modified_stack = delete_middle_element(stack)
print(modified_stack)  


# In[19]:


#Answer4:

def check_queue_order(queue):
    stack = []
    second_queue = []

    while queue:
        front_element = queue.pop(0)

        # Push front element to the second queue
        second_queue.append(front_element)

        # Check if there is a consecutive element in the second queue that is greater than the front element
        while len(second_queue) >= 2 and second_queue[-2] > second_queue[-1]:
            # Pop the last element from the second queue and push it onto the stack
            stack.append(second_queue.pop())

    # Move elements from the stack to the second queue
    while stack:
        second_queue.append(stack.pop())

    # Check if the second queue is in increasing order
    for i in range(len(second_queue) - 1):
        if second_queue[i] >= second_queue[i + 1]:
            return "No"

    return "Yes"


# Example usage:
queue = [5, 1, 2, 3, 4]
result = check_queue_order(queue)
print(result)  # Output: Yes

queue = [5, 1, 2, 6, 3, 4]
result = check_queue_order(queue)
print(result)  # Output: No


# In[20]:


#Answer5.

def reverse_number(num):
    stack = []
    result = ''

    # Convert the number to a string and push each digit onto the stack
    for digit in str(num):
        stack.append(digit)

    # Pop digits from the stack and append them to the result
    while stack:
        result += stack.pop()

    # Convert the reversed string back to an integer
    reversed_num = int(result)

    return reversed_num


# Example usage:
num = 365
reversed_num = reverse_number(num)
print(reversed_num)  

num = 6899
reversed_num = reverse_number(num)
print(reversed_num)


# In[21]:


#Answer6:


from queue import Queue

def reverse_k_elements(queue, k):
    stack = []
    temp_queue = Queue()

    # Dequeue the first k elements and push them onto the stack
    for _ in range(k):
        stack.append(queue.get())

    # Dequeue the remaining elements and enqueue them into the temporary queue
    while not queue.empty():
        temp_queue.put(queue.get())

    # Enqueue elements from the stack back into the given queue
    while stack:
        queue.put(stack.pop())

    # Enqueue elements from the temporary queue back into the given queue
    while not temp_queue.empty():
        queue.put(temp_queue.get())

    return queue


# Example usage:
queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)

k = 3
modified_queue = reverse_k_elements(queue, k)

# Print the modified queue
while not modified_queue.empty():
    print(modified_queue.get(), end=" ")


# In[22]:


#ANswer7:
def count_remaining_words(sequence):
    stack = []

    for word in sequence:
        if stack and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)

    return len(stack)


# Example usage:
sequence = ["ab", "aa", "aa", "bcd", "ab"]
remaining_words = count_remaining_words(sequence)
print(remaining_words)

sequence = ["tom", "jerry", "jerry", "tom"]
remaining_words = count_remaining_words(sequence)
print(remaining_words)


# In[23]:


#Answer 8:
def find_max_abs_difference(arr):
    n = len(arr)
    LS = [0] * n
    RS = [0] * n
    stack = []

    # Find nearest smaller element on the left side
    for i in range(n):
        while stack and stack[-1] > arr[i]:
            stack.pop()
        if stack:
            LS[i] = stack[-1]
        stack.append(arr[i])

    stack.clear()

    # Find nearest smaller element on the right side
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] > arr[i]:
            stack.pop()
        if stack:
            RS[i] = stack[-1]
        stack.append(arr[i])

    max_diff = 0

    # Calculate maximum absolute difference
    for i in range(n):
        max_diff = max(max_diff, abs(LS[i] - RS[i]))

    return max_diff


# Example usage:
arr = [2, 1, 8]
result = find_max_abs_difference(arr)
print(result) 

arr = [2, 4, 8, 7, 7, 9, 3]
result = find_max_abs_difference(arr)
print(result)  

arr = [5, 1, 9, 2, 5, 1, 7]
result = find_max_abs_difference(arr)
print(result)  


# In[ ]:




