class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        cur=dummy
        while cur.next:
            prev=cur
            if cur.next.val==0:
                cur=cur.next
            if cur.next:
                cur.val+=cur.next.val
                cur.next=cur.next.next
        prev.next=None
        return head
