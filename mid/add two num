class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        fst_num = l1
        sec_num = l2
        f_num = self.node_to_num(l1)
        s_num = self.node_to_num(l2)
        r_f_num = int(str(f_num)[::-1])
        r_s_num = int(str(s_num)[::-1])
        t_num = r_f_num+r_s_num
        target = self.num_to_node(t_num)
        return target
        
    def node_to_num(self, li: ListNode):
        digit= 1
        while(li):
            target = li.val*digit
            digit *= 10
            li = li.next
        return target
        
    def num_to_node(self,num): 
        str_num = reversed(str(num))
        
        head = None
        
        for i in str_num:            
            if not head:
                head = ListNode(i)
                cur = head
            else:
                cur.next = ListNode(i)
                cur = cur.next
        return head
