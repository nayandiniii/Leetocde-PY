class Solution(object):
    def hasCycle(self, head):
        #using tortoise and flare algorithm
        #we check if the rabbit moving two steps and tortoise moving one step
        #end at the same node or not and if they do it means the list is cycle
        rabbit=head #creating two pointers , rabbit moves two steps further
        tortoise = head  #moves one step further

        while rabbit and rabbit.next:
            rabbit=rabbit.next.next
            tortoise=tortoise.next
            if rabbit==tortoise:
                return True
        return False
