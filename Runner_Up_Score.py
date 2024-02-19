if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = list(set(arr))
    
    max_score = max(unique_scores)
    
    unique_scores.remove(max_score)
    
    runner_up_score = max(unique_scores) if unique_scores else max_score
    
    print(runner_up_score)