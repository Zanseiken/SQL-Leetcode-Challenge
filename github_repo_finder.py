#!/usr/bin/env python3
"""
GitHub Repository Finder for VLA AI Engineer Role
Searches for repositories relevant to Vision-Language-Action models and multimodal AI
with less than 100 stars to include in CV/resume.
"""

import requests
import json
import time
import os
from typing import List, Dict
from datetime import datetime


class GitHubRepoFinder:
    """Search GitHub for repositories matching VLA AI job requirements."""
    
    def __init__(self, max_stars: int = 100, github_token: str = None):
        self.base_url = "https://api.github.com/search/repositories"
        self.max_stars = max_stars
        self.results = []
        
        # Try to get GitHub token from parameter or environment
        self.github_token = github_token or os.environ.get('GITHUB_TOKEN')
        
        # Set up headers with authentication if available
        self.headers = {}
        if self.github_token:
            self.headers['Authorization'] = f'token {self.github_token}'
            print("✓ Using GitHub authentication (higher rate limits)")
        else:
            print("⚠ No GitHub token found. Using unauthenticated access (60 requests/hour)")
            print("  Set GITHUB_TOKEN environment variable for higher limits (5000 requests/hour)")
            print("  Generate token at: https://github.com/settings/tokens\n")
        
    def search_repositories(self, query: str, max_results: int = 30) -> List[Dict]:
        """
        Search GitHub repositories with the given query.
        
        Args:
            query: GitHub search query string
            max_results: Maximum number of results to return
            
        Returns:
            List of repository dictionaries
        """
        params = {
            'q': f'{query} stars:<{self.max_stars}',
            'sort': 'stars',
            'order': 'desc',
            'per_page': min(max_results, 100)
        }
        
        try:
            response = requests.get(self.base_url, params=params, headers=self.headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            repos = []
            for item in data.get('items', [])[:max_results]:
                repos.append({
                    'name': item['name'],
                    'full_name': item['full_name'],
                    'description': item.get('description', 'No description'),
                    'stars': item['stargazers_count'],
                    'language': item.get('language', 'N/A'),
                    'url': item['html_url'],
                    'topics': item.get('topics', []),
                    'updated_at': item['updated_at']
                })
            
            return repos
            
        except requests.exceptions.RequestException as e:
            if '403' in str(e):
                print(f"⚠ Rate limit exceeded or authentication required")
                print(f"  Set GITHUB_TOKEN environment variable for higher limits")
            else:
                print(f"Error searching repositories: {e}")
            return []
    
    def find_vla_repositories(self) -> List[Dict]:
        """Find repositories related to Vision-Language-Action models."""
        
        search_queries = [
            # Vision-Language-Action Models
            'vision-language-action OR VLA OR RT-2 OR OpenVLA OR PaLM-E language:Python',
            'vision-language model robotics language:Python',
            
            # Vision-Language Models
            'LLaVA OR BLIP-2 OR Florence OR Kosmos multimodal language:Python',
            'GPT-4V OR vision-language OR VLM language:Python',
            'CLIP vision transformer language:Python',
            
            # Multimodal AI and Robotics
            'multimodal AI robotics perception language:Python',
            'embodied AI navigation language:Python',
            'robot manipulation vision language:Python',
            
            # Specific Technologies
            'ROS vision perception PyTorch language:Python',
            'depth camera LiDAR perception language:Python',
            'transformer vision language grounding language:Python',
            
            # Research Areas
            'visual grounding dialogue language:Python',
            'human-robot interaction vision language:Python',
            'instruction following robotics language:Python',
        ]
        
        all_repos = []
        seen_repos = set()
        
        for query in search_queries:
            print(f"Searching: {query}")
            repos = self.search_repositories(query, max_results=20)
            
            for repo in repos:
                if repo['full_name'] not in seen_repos:
                    seen_repos.add(repo['full_name'])
                    all_repos.append(repo)
            
            # Rate limiting - be nice to GitHub API
            time.sleep(2)
        
        # Sort by stars (descending)
        all_repos.sort(key=lambda x: x['stars'], reverse=True)
        
        return all_repos
    
    def filter_by_relevance(self, repos: List[Dict]) -> List[Dict]:
        """Filter repositories by relevance to the job description."""
        
        relevant_keywords = [
            'vision', 'language', 'multimodal', 'robot', 'vla', 'vlm',
            'pytorch', 'transformer', 'clip', 'blip', 'llava', 'perception',
            'grounding', 'embodied', 'manipulation', 'navigation', 'ros',
            'depth', 'lidar', 'camera', 'action', 'control', 'dialogue'
        ]
        
        filtered = []
        for repo in repos:
            # Check if repo has relevant keywords in name, description, or topics
            text = f"{repo['name']} {repo['description']} {' '.join(repo['topics'])}".lower()
            
            keyword_matches = sum(1 for keyword in relevant_keywords if keyword in text)
            
            if keyword_matches >= 2:  # At least 2 keyword matches
                repo['relevance_score'] = keyword_matches
                filtered.append(repo)
        
        # Sort by relevance score
        filtered.sort(key=lambda x: (x['relevance_score'], x['stars']), reverse=True)
        
        return filtered
    
    def print_results(self, repos: List[Dict], output_file: str = None):
        """Print search results in a formatted way."""
        
        print(f"\n{'='*80}")
        print(f"Found {len(repos)} repositories matching VLA AI Engineer job requirements")
        print(f"(with less than {self.max_stars} stars)")
        print(f"{'='*80}\n")
        
        output_lines = []
        output_lines.append("# GitHub Repositories for VLA AI Engineer CV\n")
        output_lines.append(f"*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")
        output_lines.append(f"*Search criteria: Repositories with < {self.max_stars} stars*\n\n")
        
        for i, repo in enumerate(repos, 1):
            output = f"\n{i}. **{repo['full_name']}** ⭐ {repo['stars']}\n"
            output += f"   - **Language:** {repo['language']}\n"
            output += f"   - **Description:** {repo['description']}\n"
            output += f"   - **URL:** {repo['url']}\n"
            
            if repo.get('topics'):
                output += f"   - **Topics:** {', '.join(repo['topics'])}\n"
            
            if repo.get('relevance_score'):
                output += f"   - **Relevance Score:** {repo['relevance_score']}/10\n"
            
            print(output)
            output_lines.append(output)
        
        if output_file:
            with open(output_file, 'w') as f:
                f.writelines(output_lines)
            print(f"\n✓ Results saved to {output_file}")
    
    def export_to_json(self, repos: List[Dict], filename: str = 'vla_repos.json'):
        """Export results to JSON file."""
        with open(filename, 'w') as f:
            json.dump(repos, f, indent=2)
        print(f"✓ Results exported to {filename}")


def main():
    """Main function to run the repository finder."""
    
    print("=" * 80)
    print("GitHub Repository Finder for VLA AI Engineer Role")
    print("=" * 80)
    print("\nSearching for repositories related to:")
    print("- Vision-Language-Action Models (VLA)")
    print("- Vision-Language Models (VLM)")
    print("- Multimodal AI for Robotics")
    print("- Robot Perception and Control")
    print("- Embodied AI and Navigation")
    print("\n")
    
    # Check for GitHub token
    github_token = os.environ.get('GITHUB_TOKEN')
    
    finder = GitHubRepoFinder(max_stars=100, github_token=github_token)
    
    # Find repositories
    print("Starting search...\n")
    repos = finder.find_vla_repositories()
    
    if not repos:
        print("\n" + "=" * 80)
        print("⚠ No repositories found!")
        print("=" * 80)
        print("\nPossible reasons:")
        print("1. GitHub API rate limit exceeded")
        print("2. Network connectivity issues")
        print("3. GitHub authentication required")
        print("\nSolutions:")
        print("1. Wait 1 hour and try again (for rate limit)")
        print("2. Set GITHUB_TOKEN environment variable:")
        print("   export GITHUB_TOKEN='your_token_here'")
        print("3. Generate token at: https://github.com/settings/tokens")
        print("\nAlternatively, check EXAMPLE_REPOS.md for curated examples!")
        return
    
    # Filter by relevance
    print(f"\nFiltering {len(repos)} repositories by relevance...")
    filtered_repos = finder.filter_by_relevance(repos)
    
    # Print and export results
    finder.print_results(filtered_repos[:30], output_file='VLA_GitHub_Repos.md')
    finder.export_to_json(filtered_repos[:30], filename='vla_repos.json')
    
    print("\n" + "=" * 80)
    print("Search completed! You can now use these repositories in your CV.")
    print("=" * 80)
    print("\nRecommendations:")
    print("1. Review each repository and contribute if possible")
    print("2. Fork repositories and add your own improvements")
    print("3. Star repositories you find useful")
    print("4. Mention specific repositories in your CV/cover letter")
    print("5. Highlight any contributions or forks on your GitHub profile")


if __name__ == "__main__":
    main()
