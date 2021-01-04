import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-dead',
  styleUrls: ['./dead.component.scss'],
  templateUrl: './dead.component.html',
})
export class DeadComponent {

  @Input() public rip: number;

  constructor() { }

}
