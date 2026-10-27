class LinkedList {
    Node head;
    int count;

    public LinkedList() {
        count = 0;
    }

    public int get(int index) {
        if (index >= count) {
            return -1;
        }

        int currIndex = 0;
        Node it = head;
        while (it != null) {
            if (currIndex == index) {
                return it.data;
            }
            currIndex++;
            it = it.next;
        }

        return -1;
    }

    public void insertHead(int val) {
        var node = new Node(val, head);
        head = node;
        count++;
    }

    public void insertTail(int val) {
        if (head == null) {
            head = new Node(val);
            count++;
            return;
        }

        Node it = head;
        while (it.next != null) {
            it = it.next;
        }

        it.next = new Node(val);
        count++;
    }

    public boolean remove(int index) {
        if (index >= count) {
            return false;
        }

        if (index == 0) {
            head = head.next;
            count--;
            return true;
        }

        int currIndex = 0;
        Node it = head;
        Node prev = null;
        while (it != null) {
            if (currIndex == index) {
                prev.next = it.next;
                count--;
                return true;
            }
            currIndex++;
            prev = it;
            it = it.next;
        }

        return false;
    }

    public ArrayList<Integer> getValues() {
        var list = new ArrayList<Integer>();

        Node it = head;
        while (it != null) {
            list.add(it.data);
            it = it.next;
        }       

        return list;
    }


    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
        }

         Node(int data, Node next) {
            this.data = data;
            this.next = next;
        }       
    }
}
