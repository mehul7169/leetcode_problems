class SparseVector {
    
    private TreeMap<Integer, Integer> st;

    SparseVector(int[] nums) {
        int size = nums.length;
        st = new TreeMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                st.put(i, nums[i]);
            }
        }
    }
    
	// Return the dotProduct of two sparse vectors
    public int dotProduct(SparseVector vec) {
        TreeMap<Integer, Integer> first = this.st;
        TreeMap<Integer, Integer> second = vec.st;
        
        int count = 0;
        for (Map.Entry<Integer, Integer> elem : first.entrySet()) {
            if (second.containsKey(elem.getKey())) {
                count = count + (second.get(elem.getKey()) * elem.getValue());            
            }
        }
        return count;
    }
}