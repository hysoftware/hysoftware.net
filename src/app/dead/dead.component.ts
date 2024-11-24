import { Component, Input } from '@angular/core';

@Component({
  standalone: false,
  selector: 'app-dead',
  styleUrls: ['./dead.component.scss'],
  templateUrl: './dead.component.html',
})
export class DeadComponent {

  @Input() public rip: number;

  constructor() { }

}
