{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOYbWwFyzyIj9MPzHPD7wDR",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Gizelle-16/Gitel_Scifor/blob/main/LeetcodeAssignment.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "OzfyKK3Jx6Vx"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q1: Merge Strings Alternately"
      ],
      "metadata": {
        "id": "XCGpLkSOyFkh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Solution(object):\n",
        "    def mergeAlternately(self, word1, word2):\n",
        "        merged = \"\"\n",
        "        lenn = min(len(word1), len(word2))\n",
        "        k = 0\n",
        "        for i in range(0, lenn):\n",
        "            merged += word1[i] + word2[i]\n",
        "            k += 1\n",
        "\n",
        "        if k < len(word1):\n",
        "            for i in range(k, len(word1)):\n",
        "                merged += word1[i]\n",
        "        else:\n",
        "            for i in range(k, len(word2)):\n",
        "                merged += word2[i]\n",
        "\n",
        "        return merged\n",
        "\n",
        "obj = Solution()\n",
        "print(obj.mergeAlternately(word1=\"abcg\", word2=\"defeee\"))\n"
      ],
      "metadata": {
        "id": "xPnrYGAqyGwM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q2:  Find the Difference"
      ],
      "metadata": {
        "id": "OM4LzgxEyMJz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Solution(object):\n",
        "    def findTheDifference(self, s, t):\n",
        "        for i in range(0, len(t)):\n",
        "            count_t = t.count(t[i])\n",
        "            count_s = s.count(t[i])\n",
        "            if count_t> count_s:\n",
        "                return t[i]\n",
        "\n",
        "obj = Solution()\n",
        "print(obj.findTheDifference(s=\"gitel\", t=\"iletgg\"))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZQniUEwN0Jpu",
        "outputId": "d29a5f4d-a36f-475a-e87f-5cfd8a0e288a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "g\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q3: Valid anagram"
      ],
      "metadata": {
        "id": "PQpRi0J-4tND"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Solution(object):\n",
        "    def isAnagram(self, s, t):\n",
        "        if len(t) != len(s):\n",
        "            return False\n",
        "        else:\n",
        "            for i in range(0, len(t)):\n",
        "                count_t = t.count(t[i])\n",
        "                count_s = s.count(t[i])\n",
        "                if count_t != count_s:\n",
        "                    return False\n",
        "            return True\n",
        "\n",
        "\n",
        "obj = Solution()\n",
        "print(obj.isAnagram(s=\"rat\", t=\"car\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DVPo00WE4sY3",
        "outputId": "c68de811-d8fd-45b5-fa0f-9a1fac8a70c8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q4: Repeated substring pattern"
      ],
      "metadata": {
        "id": "B5SS11NLDWzF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        " class Solution(object):\n",
        "    def repeatedSubstringPattern(self, s):\n",
        "        length = len(s)\n",
        "\n",
        "        for i in range(1, length // 2 + 1):\n",
        "\n",
        "            if length % i == 0:\n",
        "              substring = s[:i]\n",
        "              repeated_string = substring * (length // i)\n",
        "              if repeated_string == s:\n",
        "                   return True\n",
        "\n",
        "        return False\n",
        "\n",
        "\n",
        "obj = Solution()\n",
        "print(obj.repeatedSubstringPattern(\"abcabcabc\"))  # Output: True\n",
        "print(obj.repeatedSubstringPattern(\"abab\"))       # Output: True\n",
        "print(obj.repeatedSubstringPattern(\"aba\"))        # Output: False\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CakX2liLDavB",
        "outputId": "7318e216-a0b1-44e3-da05-a2495a511950"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "True\n",
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q5: Find the Index of the First Occurrence in a String\n"
      ],
      "metadata": {
        "id": "F6PgXEbbaJmc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Solution(object):\n",
        "    def strStr(self, haystack, needle):\n",
        "      x=haystack.find(needle)\n",
        "      return x\n",
        "\n",
        "obj= Solution()\n",
        "print(obj.strStr(haystack=\"applebanana\", needle='anas'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_qgu4R8ma9Br",
        "outputId": "23b6863e-47f7-4360-9d5a-41cc91145c7a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q6: Move zeroes to the end of list"
      ],
      "metadata": {
        "id": "8c_AJd81cJ0m"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# class Solution(object):\n",
        "#     def moveZeroes(self, nums):\n",
        "#       count=0\n",
        "#       for i in nums:\n",
        "#         if i!=0:\n",
        "#           pass\n",
        "#         else:\n",
        "#           count = count+1\n",
        "#           nums.remove(i)\n",
        "\n",
        "\n",
        "#       for j in range(0, count):\n",
        "#         nums.append(0)\n",
        "#       return nums\n",
        "\n",
        "# obj=Solution()\n",
        "# print(obj.moveZeroes([0,0,1]))\n",
        "\n",
        "#was facing error in the code for half of the test cases when there were 2 0s together,\n",
        "#because i was using remove while iteration, it changes the index values\n",
        "\n",
        "class Solution(object):\n",
        "    def moveZeroes(self, nums):\n",
        "        count = 0\n",
        "        i = 0\n",
        "\n",
        "        while i < len(nums):\n",
        "            if nums[i] == 0:\n",
        "                nums.pop(i)\n",
        "                count += 1\n",
        "            else:\n",
        "                i+=1\n",
        "\n",
        "        for _ in range(count):\n",
        "            nums.append(0)\n",
        "\n",
        "        return nums\n",
        "\n",
        "obj = Solution()\n",
        "print(obj.moveZeroes([0, 0, 1]))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mUoOZ1x1d1Ki",
        "outputId": "00922835-56fe-4fc0-ac6c-120e5a9cf756"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 0, 0]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q7: Plus one"
      ],
      "metadata": {
        "id": "FEZf5q0ekfuJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Solution(object):\n",
        "    def plusOne(self, digits):\n",
        "        n = len(digits)\n",
        "\n",
        "        for i in range(n - 1, -1, -1):\n",
        "            if digits[i] < 9:\n",
        "                digits[i] += 1\n",
        "                return digits\n",
        "            else:\n",
        "                digits[i] = 0\n",
        "\n",
        "        digits.insert(0, 1)\n",
        "        return digits\n",
        "\n",
        "obj = Solution()\n",
        "result = obj.plusOne([9, 8,2])\n",
        "print(result)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F4273LAsmGsa",
        "outputId": "faf657b3-f682-44e1-d026-2044d942cb8a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[9, 8, 3]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q8: Sign of the Product of an Array\n"
      ],
      "metadata": {
        "id": "yNk5dguZq5Kd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Solution(object):\n",
        "    def arraySign(self, nums):\n",
        "        count=0\n",
        "        for i in nums:\n",
        "            if i==0:\n",
        "                return 0\n",
        "            elif i<0:\n",
        "                count+=1\n",
        "        if count%2==0:\n",
        "            return 1\n",
        "        else:\n",
        "            return -1\n"
      ],
      "metadata": {
        "id": "Y-V7u8PCq5_K"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Q9: Arithmetic progression"
      ],
      "metadata": {
        "id": "enmXHnoQr3EJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Solution(object):\n",
        "    def canMakeArithmeticProgression(self, arr):\n",
        "        arr.sort()\n",
        "        for i in range(2, len(arr)):\n",
        "            if 2 * arr[i - 1] != arr[i - 2] + arr[i]:\n",
        "                return False\n",
        "        return True\n",
        "\n",
        "obj = Solution()\n",
        "print(obj.canMakeArithmeticProgression([4, 5, 6]))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Tgq18KJJs_VO",
        "outputId": "5871efbd-8148-49be-a384-3054e3b1db56"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    }
  ]
}