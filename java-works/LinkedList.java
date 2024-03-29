public class LinkedList {
    ListNode head = null;

    public void add(int value, int index) throws BadIndexFormatException{
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
                throw new BadIndexFormatException("Please give a reachable index to set the given value.");
            }
        }
    }

    public int get(int index) throws BadIndexFormatException {
        ListNode temp = this.head;
        int count = 0;
        while(count < index && temp != null){
            temp = temp.next;
            count++;
        }
        if (temp != null){
            return temp.value;
        } else {
            throw new BadIndexFormatException("Please give a reachable index to get the value of the given index.");
        }
    }

    public void remove(int index) throws BadIndexFormatException{
        ListNode temp = this.head;
        int count = 0;
        while(count < index-1 && temp != null){
            temp = temp.next;
            count++;
        }
        if (temp != null){
            ListNode node_to_remove = temp.next;
            temp.next = node_to_remove.next;
        } else {
            throw new BadIndexFormatException("Please give a reachable index to get the value of the given index.");
        }
    }

    public void print() {
        ListNode temp = this.head;
        while (temp != null) {
            System.out.println(temp.value + ", ");
            temp = temp.next;
        }
        System.out.println();
    }

    public void addLast(int value) {
        ListNode temp = this.head;
        while(temp.next != null) {
            temp = temp,next;
        }
        ListNode mn = new ListNode();
        mn.value = value;
        mn.next = temp.next;
        temp.next = mn;
    }

    public void addFirst(int value) {
        ListNode mn = new ListNode();
        mn.value = value;
        mn.next = this.head;
        this.head = mn;
    }
}
