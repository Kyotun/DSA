public class LinkedList {
    ListNode head = null;

    public void add(int value, int index) {
        if (head == null) {
            this.head = new ListNode();
            this.head.value = value;
        } else if (index == 0) {
            ListNode ml = new ListNode();
            ml.value = value;
            ml.next = this.head;
            this.head = ml;
        } else {
            ListNode temp = this.head;
            int count = 1;
            while(count < index && temp != null) {
                temp = temp.next;
                count++;
            }
            if(temp != null){
                ListNode ml = new ListNode();
                ml.value = value;
                ml.next = temp.next;
                temp.next = ml;
            } else {
                System.out.println("Index is out of range.");
            }
        }
    }
}
