class DynamicArray {
    int capacity;
    int count;
    int[] array;

    public DynamicArray(int capacity) {
        array = new int[capacity];
        this.capacity = capacity;
        this.count = 0;
    }

    public int get(int i) {
        if (i >= count) {
            throw new RuntimeException();
        }

        return array[i];
    }

    public void set(int i, int n) {
        if (i >= count) {
            throw new RuntimeException();
        }

        array[i] = n;
    }

    public void pushback(int n) {
        // Need to resize?
        if (count == capacity) {
            resize();
        }

        array[count] = n;
        count++;
    }

    public int popback() {
        int temp = array[count - 1];
        array[count - 1] = 0;
        count--;
        return temp;
    }

    private void resize() {
        int newCap = capacity * 2;
        int[] newArray = new int[newCap];
        for (int i = 0; i < count; i++) {
            newArray[i] = array[i];
        }
        array = newArray;
        capacity = newCap;
    }

    public int getSize() {
        return count;
    }

    public int getCapacity() {
        return capacity;
    }
}
