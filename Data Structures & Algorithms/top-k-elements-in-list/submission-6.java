class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freq = new HashMap<>();

        ArrayList<Integer>[] bucket = new ArrayList[nums.length + 1];

        for(int i = 0; i < nums.length; i++) {
            if(freq.containsKey(nums[i])) {
                freq.put(nums[i], freq.get(nums[i]) + 1);
            } else {
                freq.put(nums[i], 1);
            }
        }
        for (int i = 0; i <= nums.length; i++) {
            bucket[i] = new ArrayList<>();
        }
        for (int n : freq.keySet()) {
            bucket[freq.get(n)].add(n);
        }

        int[] result = new int[k];
        int idx = 0;

        for(int i = bucket.length - 1; i >= 0; i--) {
            for (int n : bucket[i]) {
                result[idx] = n;
                idx++;
                if(idx == k) break;
            }
            if(idx == k) break;
        }
        return result;
    }
}
