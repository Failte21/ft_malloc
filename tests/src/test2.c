/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test2.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lsimon <lsimon@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/14 12:05:14 by lsimon            #+#    #+#             */
/*   Updated: 2018/09/14 12:42:18 by lsimon           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../malloc.h"

int main(void)
{
   int   i;
   char  *addr;

   i = 0;
   addr = NULL;
   while (i < 1024)
   {
      addr = (char*)malloc(1024);
      addr[0] = 42;
      i++;
   }
   return (0);
}